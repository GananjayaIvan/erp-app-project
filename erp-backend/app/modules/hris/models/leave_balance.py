from .library.dependencies import *

class LeaveBalance(Base):
    __tablename__ = "leave_balance"

    id = Column(Integer, primary_key=True, index=True)

    employee_id = Column(Integer, ForeignKey("employee.id"), nullable=False)
    leave_type_id = Column(Integer, ForeignKey("leave_type.id"), nullable=False)

    year = Column(Integer, nullable=False)

    allocated_days = Column(Integer, default=0)
    used_days = Column(Integer, default=0)

    # Relationships
    employee = relationship("Employee")
    leave_type = relationship("LeaveType")