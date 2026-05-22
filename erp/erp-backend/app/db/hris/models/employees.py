from .library.dependencies import *
from app.db.hris.enums.employment_status import EmploymentStatus


class Employees(Base):
    __tablename__ = "employees"

    __table_args__ = {"schema": "hris"}
    
    # IDENTITY
    
    id = Column(Integer, primary_key=True, index=True)

    employee_number = Column(
    String,
    unique=True,
    index=True,
    nullable=False
    )

    full_name = Column(String, nullable=False)

    status = Column(
        SQLEnum(EmploymentStatus, name="employee_status"),
        default=EmploymentStatus.active,
        nullable=False,
        index=True
    )

    joined_at = Column(DateTime, nullable=True,index=True)
    terminated_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, server_default=func.now())

    
    # AUTH    
    user = relationship(
        "User",
        back_populates="employee",
        uselist=False
    )

    
    # ORGANIZATION ACCESS (M2M)
    
    organizations = relationship(
        "EmployeeOrganization",
        back_populates="employee",
        cascade="all, delete-orphan"
    )

    
    # EMPLOYMENT (ORG CONTEXT LAYER)
    
    employments = relationship(
        "EmploymentModels",
        back_populates="employee",
        cascade="all, delete-orphan"
    )

    
    # OPTIONAL LEGACY RELATIONS
    
    attendances = relationship(
        "Attendance",
        back_populates="employee"
    )

    salaries = relationship(
        "Salary",
        back_populates="employee"
    )
    
    sensitive = relationship(
        "EmployeeSensitive",
        back_populates="employee",
        uselist=False,
        cascade="all, delete-orphan"
    )