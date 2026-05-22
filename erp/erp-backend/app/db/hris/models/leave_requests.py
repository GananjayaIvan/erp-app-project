from .library.dependencies import *
from app.db.hris.enums.leave_request_status import *

class LeaveRequests(Base):
    __tablename__ = "leave_requests"

    __table_args__ = {"schema": "hris"}

    
    # IDENTITY
    id = Column(Integer, primary_key=True, index=True)

    
    # ORG CONTEXT
    
    organization_id = Column(
        Integer,
        ForeignKey("hris.organizations.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    
    # CORE RELATION
    
    employment_id = Column(
        Integer,
        ForeignKey("hris.employment_models.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    leave_types_id = Column(
        Integer,
        ForeignKey("hris.leave_types.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    
    # LEAVE DETAILS
    
    start_date = Column(DateTime, nullable=False)

    end_date = Column(DateTime, nullable=False)

    total_days = Column(Integer, nullable=False)

    reason = Column(String, nullable=True)

    
    # STATUS
    
    status = Column(
        SQLEnum(
            LeaveRequestStatus,
            name="leave_request_status"
        ),
        default=LeaveRequestStatus.pending,
        nullable=False,
        index=True
    )

    
    # APPROVAL FLOW
    
    approved_by_employment_id = Column(
        Integer,
        ForeignKey("hris.employment_models.id"),
        nullable=True,
        index=True
    )

    approved_at = Column(DateTime, nullable=True)

    rejection_reason = Column(String, nullable=True)

    
    # AUDIT
    
    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

    
    # RELATIONSHIPS
    
    employment = relationship(
        "EmploymentModels",
        foreign_keys=[employment_id],
        backref="leave_requests"
    )

    leave_types = relationship(
        "LeaveType",
        backref="leave_requests"
    )

    organization = relationship(
        "Organization",
        backref="leave_requests"
    )

    approver = relationship(
        "EmploymentModels",
        foreign_keys=[approved_by_employment_id],
        backref="approved_leave_requests"
    )