from .library.dependencies import *
from enum import Enum


class OfficeTypeEnum(str, Enum):
    hq = "hq"
    branch = "branch"
    remote = "remote"
    warehouse = "warehouse"


class Offices(Base):
    __tablename__ = "offices"

    
    # IDENTITY
    
    id = Column(Integer, primary_key=True, index=True)

    code = Column(String(50), unique=True, index=True, nullable=False)

    name = Column(String(255), nullable=False)

    
    # ORG CONTEXT (SAAS FIX)
    
    organization_id = Column(
        Integer,
        ForeignKey("organizations.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    
    # LOCATION
    
    address = Column(String(255), nullable=True)

    city = Column(String(100), nullable=True)

    state = Column(String(100), nullable=True)

    country = Column(String(100), nullable=True)

    postal_code = Column(String(20), nullable=True)

    latitude = Column(Float, nullable=True)

    longitude = Column(Float, nullable=True)

    timezone = Column(String(50), default="Asia/Jakarta")

    
    # HIERARCHY
    
    parent_id = Column(
        Integer,
        ForeignKey("offices.id"),
        nullable=True,
        index=True
    )

    parent = relationship(
        "Offices",
        remote_side=[id],
        backref="children",
        foreign_keys=[parent_id],
    )

    
    # TYPE / STATUS
    
    offices_type = Column(
        SQLEnum(OfficeTypeEnum, name="office_type_enum"),
        nullable=True,
        index=True
    )

    is_active = Column(Boolean, default=True, index=True)

    
    # AUDIT
    
    created_at = Column(DateTime, server_default=func.now())

    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    
    # RELATIONSHIPS
    
    employees = relationship("Employees", back_populates="offices")

    
    # DERIVED FIELD (SAFE VERSION)
    
    def get_level(self) -> int:
        """
        Safe non-recursive level calculation.
        """
        level = 1
        current = self.parent

        while current:
            level += 1
            current = current.parent

        return level

    
    # VALIDATION
    
    def validate_hierarchy(self):
        if self.parent_id is not None and self.parent_id == self.id:
            raise ValueError("Office cannot be its own parent")

        if self._creates_cycle():
            raise ValueError("Circular hierarchy detected")

    
    # CYCLE DETECTION
    
    def _creates_cycle(self) -> bool:
        current = self.parent

        while current:
            if current.id == self.id:
                return True
            current = current.parent

        return False

    
    # SAFE TREE OPERATIONS
    
    def get_root(self):
        current = self
        while current.parent:
            current = current.parent
        return current

    def get_ancestors(self):
        ancestors = []
        current = self.parent

        while current:
            ancestors.append(current)
            current = current.parent

        return ancestors

    def get_descendants(self):
        """
        Iterative DFS (safer than recursion).
        """
        result = []
        stack = list(self.children)

        while stack:
            node = stack.pop()
            result.append(node)
            stack.extend(node.children)

        return result