# app/modules/hris/models/employment_model.py

from enum import Enum as PyEnum

from .library.dependencies import (
    Base,
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    relationship,
    func,
    SQLEnum,
)


# =========================
# ENUM: Employment Status
# =========================
class EmploymentStatus(str, PyEnum):
    active = "active"
    resigned = "resigned"
    terminated = "terminated"
    suspended = "suspended"


# =========================
# ENUM: Employment Type
# =========================
class EmploymentType(str, PyEnum):
    permanent = "permanent"
    contract = "contract"
    intern = "intern"


# =========================
# MODEL
# =========================
class EmploymentModel(Base):
    __tablename__ = "employment_model"

    id = Column(Integer, primary_key=True, index=True)

    # =========================
    # RELATIONS
    # =========================
    employee_id = Column(
        Integer,
        ForeignKey("employee.id"),
        nullable=False,
        index=True,
    )

    position_id = Column(
        Integer,
        ForeignKey("employee_position.id"),
        nullable=False,
    )

    office_id = Column(
        Integer,
        ForeignKey("office.id"),
        nullable=False,
    )

    manager_id = Column(
        Integer,
        ForeignKey("employee.id"),
        nullable=True,
    )

    employee = relationship(
        "Employee",
        back_populates="employments",
        foreign_keys=[employee_id],
    )

    manager = relationship(
        "Employee",
        foreign_keys=[manager_id],
    )

    position = relationship("Position", backref="employments")
    office = relationship("Office", backref="employments")

    # =========================
    # TIMELINE
    # =========================
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=True)

    # =========================
    # CLASSIFICATION
    # =========================
    status = Column(
        SQLEnum(EmploymentStatus, name="employment_status"),
        default=EmploymentStatus.active,
        nullable=False,
    )

    employment_type = Column(
        SQLEnum(EmploymentType, name="employment_type"),
        nullable=True,
    )

    # =========================
    # SNAPSHOT (HISTORY SAFETY)
    # =========================
    position_snapshot = Column(String, nullable=True)
    office_snapshot = Column(String, nullable=True)

    # =========================
    # AUDIT
    # =========================
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
    )