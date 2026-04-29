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
