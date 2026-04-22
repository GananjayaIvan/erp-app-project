from .library.dependencies import *
class LeaveRequest(Base):
    __tablename__ = "leave_request"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employee.id"), nullable=False, index=True)

    leave_type_id = Column(Integer, ForeignKey("leave_type.id"), nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)

    total_days = Column(Integer, nullable=False)
    reason = Column(String, nullable=True)

    status = Column(String, default="pending")
    # pending | approved | rejected | cancelled

    approved_by = Column(Integer, ForeignKey("employee.id"), nullable=True)
    approved_at = Column(DateTime, nullable=True)

    rejection_reason = Column(String, nullable=True)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    employee = relationship(
        "Employee",
        foreign_keys=[employee_id],
        backref="leave_requests"
    )

    approver = relationship(
        "Employee",
        foreign_keys=[approved_by]
    )

    leave_type = relationship("LeaveType")