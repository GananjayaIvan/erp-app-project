from .library.dependencies import *


class EmployeeStatus(PyEnum):
    active = "active"
    inactive = "inactive"
    terminated = "terminated"
    suspended = "suspended"

class Employee(Base):
    __tablename__ = "employee"


    # Identity

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String, nullable=False)

    email = Column(String, unique=True, index=True, nullable=False)

    phone = Column(String, nullable=True)

    date_of_birth = Column(DateTime, nullable=True)

    gender = Column(String, nullable=True)


    # Lifecycle

    status = Column(
        SQLEnum(EmployeeStatus, name="employee_status"),
        default=EmployeeStatus.active,
        nullable=False
    )

    joined_at = Column(DateTime, nullable=True)
    terminated_at = Column(DateTime, nullable=True)


    # System

    created_at = Column(DateTime, server_default=func.now())


    # Org hierarchy

    manager_id = Column(
        Integer,
        ForeignKey("employee.id", ondelete="SET NULL"),
        nullable=True,
        index=True
    )

    manager = relationship(
        "Employee",
        remote_side=[id],
        backref="subordinates"
    )


    # Auth

    auth = relationship(
        "EmployeeAuth",
        back_populates="employee",
        uselist=False
    )


    # HR relations

    employments = relationship(
        "Employment",
        back_populates="employee",
        cascade="all, delete-orphan"
    )

    attendances = relationship(
        "Attendance",
        back_populates="employee"
    )