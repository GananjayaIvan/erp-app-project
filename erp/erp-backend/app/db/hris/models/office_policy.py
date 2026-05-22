from .library.dependencies import *
from enum import Enum


class ShiftTypeEnum(str, Enum):
    fixed = "fixed"
    shift = "shift"
    flexible = "flexible"
    full_24_7 = "24_7"


class OfficePolicy(Base):
    __tablename__ = "offices_policy"

    __table_args__ = {"schema": "hris"}
    
    # IDENTITY
    
    id = Column(Integer, primary_key=True)

    
    # ORG CONTEXT (IMPORTANT FOR SAAS)
    
    organization_id = Column(
        Integer,
        ForeignKey("hris.organizations.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    
    # CORE RELATION
    
    offices_id = Column(
        Integer,
        ForeignKey("hris.offices.id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
        index=True
    )

    offices = relationship(
        "Offices",
        back_populates="policy",
        uselist=False
    )

    
    # WORK SCHEDULE CONFIG
    
    working_days = Column(JSON, nullable=False)
    # expected: ["mon","tue","wed","thu","fri"]

    working_hours_start = Column(Time, nullable=True)
    working_hours_end = Column(Time, nullable=True)

    shift_type = Column(
        SQLEnum(ShiftTypeEnum, name="shift_type_enum"),
        nullable=False,
        default=ShiftTypeEnum.fixed,
        index=True
    )

    
    # RULES
    
    late_grace_minutes = Column(Integer, default=10, nullable=False)

    overtime_enabled = Column(Boolean, default=True, nullable=False)

    
    # AUDIT
    
    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )
