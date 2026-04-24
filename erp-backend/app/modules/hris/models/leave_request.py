from .library.dependencies import *
from app.modules.hris.enums.leave_request_status import *

class LeaveRequest(Base):
    __tablename__ = "leave_requests"

    # =========================
    # IDENTITY
    # =========================
    id = Column(Integer, primary_key=True, index=True)

    # =========================
    # ORG CONTEXT
    # =========================
    organization_id = Column(
        Integer,
        ForeignKey("organizations.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    # =========================
    # CORE RELATION
    # =========================
    employment_id = Column(
        Integer,
        ForeignKey("employments.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    leave_type_id = Column(
        Integer,
        ForeignKey("leave_type.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    # =========================
    # LEAVE DETAILS
    # =========================
    start_date = Column(DateTime, nullable=False)

    end_date = Column(DateTime, nullable=False)

    total_days = Column(Integer, nullable=False)

    reason = Column(String, nullable=True)

    # =========================
    # STATUS
    # =========================
    status = Column(
        SQLEnum(
            LeaveRequestStatus,
            name="leave_request_status"
        ),
        default=LeaveRequestStatus.pending,
        nullable=False,
        index=True
    )

    # =========================
    # APPROVAL FLOW
    # =========================
    approved_by_employment_id = Column(
        Integer,
        ForeignKey("employments.id"),
        nullable=True,
        index=True
    )

    approved_at = Column(DateTime, nullable=True)

    rejection_reason = Column(String, nullable=True)

    # =========================
    # AUDIT
    # =========================
    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

    # =========================
    # RELATIONSHIPS
    # =========================
    employment = relationship(
        "EmploymentModel",
        foreign_keys=[employment_id],
        backref="leave_requests"
    )

    leave_type = relationship(
        "LeaveType",
        backref="leave_requests"
    )

    organization = relationship(
        "Organization",
        backref="leave_requests"
    )

    approver = relationship(
        "EmploymentModel",
        foreign_keys=[approved_by_employment_id],
        backref="approved_leave_requests"
    )