from .library.dependencies import *
from app.db.hris.enums.employment_status import *

class EmploymentModels(Base):
    __tablename__ = "employment_models"

    __table_args__ = (
        UniqueConstraint(
            "employees_id",
            "organization_id",
            name="uq_employee_org_employment"
        ),
    )

    # IDENTITY
    
    id = Column(Integer, primary_key=True, index=True)

    
    # ORG CONTEXT
    
    organization_id = Column(
        Integer,
        ForeignKey("organizations.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    
    # CORE RELATIONS
    
    employees_id = Column(
        Integer,
        ForeignKey("employees.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    position_id = Column(
        Integer,
        ForeignKey("employees_position.id"),
        nullable=False,
    )

    offices_id = Column(
        Integer,
        ForeignKey("offices.id"),
        nullable=False,
    )

    manager_employment_id = Column(
        Integer,
        ForeignKey("employment_models.id", ondelete="SET NULL"),
        nullable=True,
        index=True
    )

    
    # RELATIONSHIPS
    
    employee = relationship(
        "Employees",
        back_populates="employment_models",
        foreign_keys=[employees_id],
    )

    organization = relationship("Organization")

    position = relationship("Position", backref="employment_models")

    offices = relationship("Offices", backref="employment_models")

    manager = relationship(
        "EmploymentModel",
        remote_side=[id],
        back_populates="subordinates",
        foreign_keys=[manager_employment_id],
    )

    subordinates = relationship(
        "EmploymentModel",
        back_populates="manager"
    )

    
    # TIMELINE
    
    start_date = Column(DateTime, nullable=False)

    end_date = Column(DateTime, nullable=True)

    
    # CLASSIFICATION
    
    status = Column(
        SQLEnum(EmploymentStatus, name="employment_status"),
        default=EmploymentStatus.active,
        nullable=False,
        index=True
    )

    employment_type = Column(
        SQLEnum(EmploymentType, name="employment_type"),
        nullable=True,
    )

    
    # SNAPSHOT (HISTORY SAFETY)
    
    position_snapshot = Column(String, nullable=True)

    offices_snapshot = Column(String, nullable=True)

    
    # AUDIT
    
    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )