from .library.dependencies import *
from enum import Enum


class OrganizationStatus(str, Enum):
    active = "active"
    suspended = "suspended"
    trial = "trial"
    archived = "archived"


class Organization(Base):
    __tablename__ = "organizations"

    __table_args__ = {"schema": "hris"}

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)
    code = Column(String, unique=True, index=True, nullable=False)

    # SaaS tenant group (mandatory)
    group_id = Column(
        Integer,
        ForeignKey("hris.organization_groups.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    status = Column(
        SQLEnum(OrganizationStatus, name="organization_status"),
        default=OrganizationStatus.active,
        nullable=False,
        index=True
    )

    timezone = Column(String, default="Asia/Jakarta")
    currency = Column(String(10), default="IDR")

    is_deleted = Column(Boolean, default=False, index=True)

    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

    # Relationships
    group = relationship("OrganizationGroup", back_populates="organizations")

    members = relationship("EmployeeOrganization", back_populates="organization")
    offices = relationship("Offices", back_populates="organization")
    employments = relationship("EmploymentModel", back_populates="organization")
    leave_requests = relationship("LeaveRequest", back_populates="organization")
    leave_types = relationship("LeaveType", back_populates="organization")