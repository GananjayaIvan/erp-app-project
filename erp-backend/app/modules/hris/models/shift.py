from .library.dependencies import *
from enum import Enum


class ShiftTypeEnum(str, Enum):
    fixed = "fixed"
    flexible = "flexible"
    split = "split"
    night = "night"


class Shift(Base):
    __tablename__ = "shift"

    # =========================
    # IDENTITY
    # =========================
    id = Column(Integer, primary_key=True, index=True)

    # =========================
    # SAAS CONTEXT (IMPORTANT FIX)
    # =========================
    organization_id = Column(
        Integer,
        ForeignKey("organizations.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    offices_id = Column(
        Integer,
        ForeignKey("offices.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    # =========================
    # CORE DATA
    # =========================
    name = Column(String(100), nullable=False)

    description = Column(String(255), nullable=True)

    shift_code = Column(String(50), nullable=True, index=True)

    # =========================
    # SHIFT TIMING
    # =========================
    start_time = Column(Time, nullable=False)

    end_time = Column(Time, nullable=False)

    break_minutes = Column(Integer, default=0, nullable=False)

    timezone = Column(String(50), nullable=True)

    # =========================
    # SHIFT TYPE (IMPROVED DESIGN)
    # =========================
    shift_type = Column(
        SQLEnum(ShiftTypeEnum, name="shift_type_enum"),
        default=ShiftTypeEnum.fixed,
        nullable=False,
        index=True
    )

    is_active = Column(Boolean, default=True, index=True)

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
    organization = relationship("Organization")

    offices = relationship(
        "Offices",
        back_populates="shifts"
    )

    attendances = relationship(
        "Attendance",
        back_populates="shift"
    )

    # =========================
    # VALIDATION
    # =========================
    def validate(self):
        if self.start_time == self.end_time:
            raise ValueError("Shift start and end time cannot be the same")

        if self.break_minutes < 0:
            raise ValueError("Break minutes cannot be negative")

        if self.break_minutes > 240:
            raise ValueError("Break minutes too large")

        # Auto-detect night shift safely
        if self.start_time > self.end_time:
            self.shift_type = ShiftTypeEnum.night