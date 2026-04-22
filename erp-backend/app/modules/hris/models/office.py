from .library.dependencies import *
class Office(Base):
    __tablename__ = "office"

    
    # Identity
    
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(50), unique=True, index=True, nullable=False)
    name = Column(String(255), nullable=False)

    
    # Location
    
    address = Column(String(255), nullable=True)
    city = Column(String(100), nullable=True)
    state = Column(String(100), nullable=True)
    country = Column(String(100), nullable=True)
    postal_code = Column(String(20), nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    # Hierarchy (Adjacency List)
    
    parent_id = Column(Integer, ForeignKey("office.id"), nullable=True)

    parent = relationship(
        "Office",
        remote_side=[id],
        backref="children",
        foreign_keys=[parent_id],
    )

    office_type = Column(String(50))  # or Enum
    timezone = Column(String(50), default="Asia/Jakarta")
    
    # Status
    
    is_active = Column(Boolean, default=True)

    
    # Audit
    
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    
    # Relationships
    
    employees = relationship("Employee", back_populates="office")

    
    # DERIVED FIELD: LEVEL (NOT STORED)
    
    @property
    def level(self) -> int:
        """
        Compute hierarchy depth dynamically.
        Root = 1, child = parent + 1, etc.
        """
        if not self.parent:
            return 1
        return self.parent.level + 1

    
    # VALIDATION
    
    def validate_hierarchy(self):
        """
        Call this in service layer before insert/update.
        Ensures tree integrity.
        """

        # 1. Cannot be its own parent
        if self.parent_id is not None and self.parent_id == self.id:
            raise ValueError("Office cannot be its own parent")

        # 2. Ensure no circular reference
        if self._creates_cycle():
            raise ValueError("Circular hierarchy detected")

        # 3. Root validation
        if self.parent is None:
            # Root must conceptually be level 1 (derived check)
            return

        # 4. Optional rule: enforce strict depth difference
        # (parent-child consistency is naturally ensured by derived level)

    
    # CYCLE DETECTION
    
    def _creates_cycle(self) -> bool:
        """
        Walk up the parent chain to ensure no loops exist.
        """
        current = self.parent

        while current is not None:
            if current.id == self.id:
                return True
            current = current.parent

        return False

    
    # UTILITY HELPERS
    
    def get_root(self):
        """
        Returns the top-most ancestor office.
        """
        current = self
        while current.parent is not None:
            current = current.parent
        return current

    def get_ancestors(self):
        """
        Returns list of all parents up to root.
        """
        ancestors = []
        current = self.parent

        while current is not None:
            ancestors.append(current)
            current = current.parent

        return ancestors

    def get_descendants(self):
        """
        DFS traversal for all children.
        """
        result = []

        def dfs(node):
            for child in node.children:
                result.append(child)
                dfs(child)

        dfs(self)
        return result