from .library.dependencies import *
from enum import Enum


class ShiftTypeEnum(str, Enum):
    fixed = "fixed"
    shift = "shift"
    flexible = "flexible"
    full_24_7 = "24_7"


class OfficePolicy(Base):
    __tablename__ = "offices_policy"

    # =========================
    # IDENTITY
    # =========================
    id = Column(Integer, primary_key=True)

    # =========================
    # ORG CONTEXT (IMPORTANT FOR SAAS)
    # =========================
    organization_id = Column(
        Integer,
        ForeignKey("organizations.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    # =========================
    # CORE RELATION
    # =========================
    offices_id = Column(
        Integer,
        ForeignKey("offices.id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
        index=True
    )

    offices = relationship(
        "Offices",
        back_populates="policy",
        uselist=False
    )

    # =========================
    # WORK SCHEDULE CONFIG
    # =========================
    working_days = Column(JSON, nullable=False)
    # expected: ["mon","tue","wed","thu","fri"]

    working_hours_start = Column(Time, nullable=True)
    working_hours_end = Column(Time, nullable=True)

    shift_type = Column(
        SQLEnum(ShiftTypeEnum, name="shift_type_enum"),
        nullable=False,
        default=ShiftTypeEnum.fixed,
        index=True
    )

    # =========================
    # RULES
    # =========================
    late_grace_minutes = Column(Integer, default=10, nullable=False)

    overtime_enabled = Column(Boolean, default=True, nullable=False)

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
    # VALIDATION LOGIC
    # =========================
    def validate(self):
        allowed_days = {"mon", "tue", "wed", "thu", "fri", "sat", "sun"}

        if not self.working_days:
            raise ValueError("working_days cannot be empty")

        invalid_days = set(self.working_days) - allowed_days
        if invalid_days:
            raise ValueError(f"Invalid working days: {invalid_days}")

        if self.shift_type == ShiftTypeEnum.full_24_7:
            return

        if self.shift_type == ShiftTypeEnum.fixed:
            if not self.working_days:
                raise ValueError("Fixed shift must define working days")

        if self.working_hours_start and self.working_hours_end:
            if self.working_hours_start >= self.working_hours_end:
                raise ValueError("Start time must be before end time")