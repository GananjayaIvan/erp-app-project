from .library.dependencies import *
from app.modules.hris.enums.employment_status import EmploymentStatus


class Employees(Base):
    __tablename__ = "employees"

    # =========================
    # IDENTITY
    # =========================
    id = Column(Integer, primary_key=True, index=True)

    user_id = ForeignKey("users.id", nullable=True)

    full_name = Column(String, nullable=False)

    email = Column(String, unique=True, index=True, nullable=False)

    phone = Column(String, nullable=True)

    date_of_birth = Column(DateTime, nullable=True)

    gender = Column(String, nullable=True)

    status = Column(
        SQLEnum(EmploymentStatus, name="employee_status"),
        default=EmploymentStatus.active,
        nullable=False,
        index=True
    )

    joined_at = Column(DateTime, nullable=True)
    terminated_at = Column(DateTime, nullable=True)

    created_at = Column(DateTime, server_default=func.now())

    # =========================
    # AUTH
    # =========================
    users = relationship(
        "users",
        back_populates="employees",
        uselist=False,
        cascade="all, delete-orphan"
    )

    # =========================
    # ORGANIZATION ACCESS (M2M)
    # =========================
    organizations = relationship(
        "EmployeeOrganization",
        back_populates="employee",
        cascade="all, delete-orphan"
    )

    # =========================
    # EMPLOYMENT (ORG CONTEXT LAYER)
    # =========================
    employments = relationship(
        "EmploymentModel",
        back_populates="employee",
        cascade="all, delete-orphan"
    )

    # =========================
    # OPTIONAL LEGACY RELATIONS
    # =========================
    attendances = relationship(
        "Attendance",
        back_populates="employee"
    )

    salaries = relationship(
        "Salary",
        back_populates="employee"
    )

    # =========================
    # HELPERS
    # =========================
    def is_active(self) -> bool:
        return self.status == EmploymentStatus.active

    def is_inactive(self) -> bool:
        return self.status == EmploymentStatus.inactive

    def is_terminated(self) -> bool:
        return self.status == EmploymentStatus.terminated

    def is_suspended(self) -> bool:
        return self.status == EmploymentStatus.suspended