from .library.dependencies import *

class EmployeeOrganizations(Base):
    __tablename__ = "employee_organizations"

    __table_args__ = (
        UniqueConstraint("employee_id", "organization_id", name="uq_employee_org"),
        {"schema": "hris"}
    )

    id = Column(Integer, primary_key=True)

    employee_id = Column(
        Integer,
        ForeignKey("hris.employees.id", ondelete="CASCADE"),
        nullable=False
    )

    organization_id = Column(
        Integer,
        ForeignKey("hris.organizations.id", ondelete="CASCADE"),
        nullable=False
    )

    role = Column(String, nullable=False, default="member")
    is_active = Column(Boolean, default=True)

    joined_at = Column(DateTime, server_default=func.now())

    # relationships
    employee = relationship("Employees", back_populates="organizations")
    organization = relationship("Organization", back_populates="members")
