from .library.dependencies import *

class LeaveType(Base):
    __tablename__ = "leave_type"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)
    # e.g. Annual Leave, Sick Leave, Maternity Leave

    code = Column(String(50), unique=True, nullable=False)
    # e.g. AL, SL, ML

    description = Column(String, nullable=True)

    is_paid = Column(Boolean, default=True)
    requires_attachment = Column(Boolean, default=False)
    # e.g. sick leave may require medical certificate

    max_days_per_year = Column(Integer, nullable=True)
    # null = unlimited

    max_consecutive_days = Column(Integer, nullable=True)
    carry_forward_allowed = Column(Boolean, default=False)
    carry_forward_limit = Column(Integer, nullable=True)

    is_active = Column(Boolean, default=True)
    is_emergency = Column(Boolean, default=False)
    # e.g. urgent leave type that bypasses some rules

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # 🔗 Relationships
    leave_requests = relationship("LeaveRequest", back_populates="leave_type")