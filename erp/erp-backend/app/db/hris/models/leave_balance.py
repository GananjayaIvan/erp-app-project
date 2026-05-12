from .library.dependencies import *


class LeaveBalance(Base):
    __tablename__ = "leave_balance"

    
    # IDENTITY
    
    id = Column(Integer, primary_key=True, index=True)

    
    # ORG CONTEXT (IMPORTANT)
    
    organization_id = Column(
        Integer,
        ForeignKey("organizations.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    
    # CORE RELATION (IMPORTANT FIX)
    
    employment_id = Column(
        Integer,
        ForeignKey("employment_models.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    leave_types_id = Column(
        Integer,
        ForeignKey("leave_types.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    
    # TIME DATA
    
    year = Column(Integer, nullable=False, index=True)

    
    # BALANCE DATA
    
    allocated_days = Column(Integer, default=0, nullable=False)

    used_days = Column(Integer, default=0, nullable=False)

    
    # AUDIT
    
    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

    
    # RELATIONSHIPS
    
    employment = relationship("EmploymentModel")
    leave_types = relationship("LeaveType")
    organization = relationship("Organization")