from .library.dependencies import *


class LeaveType(Base):
    __tablename__ = "leave_type"

    
    # IDENTITY
    
    id = Column(Integer, primary_key=True, index=True)

    
    # ORG CONTEXT (IMPORTANT FIX FOR SAAS)
    
    organization_id = Column(
        Integer,
        ForeignKey("organizations.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    
    # CORE DATA
    
    name = Column(String(100), nullable=False)
    # e.g. Annual Leave, Sick Leave, Maternity Leave

    code = Column(String(50), nullable=False, index=True)
    # e.g. AL, SL, ML (NOT global unique anymore → org-scoped)

    description = Column(String, nullable=True)

    
    # RULES / POLICY
    
    is_paid = Column(Boolean, default=True, nullable=False)

    requires_attachment = Column(Boolean, default=False, nullable=False)

    max_days_per_year = Column(Integer, nullable=True)

    max_consecutive_days = Column(Integer, nullable=True)

    carry_forward_allowed = Column(Boolean, default=False, nullable=False)

    carry_forward_limit = Column(Integer, nullable=True)

    is_emergency = Column(Boolean, default=False, nullable=False)

    is_active = Column(Boolean, default=True, index=True, nullable=False)

    
    # AUDIT
    
    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

    
    # RELATIONSHIPS
    
    organization = relationship("Organization")

    leave_requests = relationship(
        "LeaveRequest",
        back_populates="leave_type",
        cascade="all"
    )