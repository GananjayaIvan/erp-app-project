from .library.dependencies import *
from enum import Enum


from .library.dependencies import *


class OrganizationGroup(Base):
    __tablename__ = "organization_groups"

    # =========================
    # IDENTITY
    # =========================
    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(255), nullable=False)
    code = Column(String(100), unique=True, nullable=False, index=True)

    description = Column(String, nullable=True)

    # =========================
    # SAAS STATUS (OPTIONAL CONTROL)
    # =========================
    is_active = Column(Boolean, default=True, index=True)

    # You can expand later:
    # trial, paid, suspended billing, etc.
    status = Column(String(50), default="active", index=True)

    # =========================
    # BILLING / SAAS EXTENSION READY
    # =========================
    subscription_plan = Column(String(50), nullable=True)
    billing_email = Column(String(255), nullable=True)

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

    # One group → many organizations
    organizations = relationship(
        "Organization",
        back_populates="group",
        cascade="all, delete-orphan"
    )

    # =========================
    # HELPERS
    # =========================

    def is_active_group(self) -> bool:
        return self.is_active and self.status == "active"