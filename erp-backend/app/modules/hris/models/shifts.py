from .library.dependencies import *
from app.modules.hris.enums.attendance import *
from datetime import datetime, timedelta


class Shift(Base):
    __tablename__ = "shift"


    # IDENTITY

    id = Column(Integer, primary_key=True, index=True)


    # SAAS CONTEXT

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


    # CORE DATA

    name = Column(String(100), nullable=False)
    description = Column(String(255))
    shift_code = Column(String(50), index=True)


    # SHIFT TIMING

    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)

    break_minutes = Column(Integer, default=0, nullable=False)

    timezone = Column(String(50), nullable=True)

    grace_before_minutes = Column(Integer, default=30, nullable=False)
    grace_after_minutes = Column(Integer, default=10, nullable=False)


    # SHIFT TYPE

    shift_type = Column(
        SQLEnum(ShiftTypeEnum, name="shift_type_enum"),
        default=ShiftTypeEnum.fixed,
        nullable=False,
        index=True
    )

    is_active = Column(Boolean, default=True)


    # AUDIT

    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)


    # RELATIONSHIPS (FIXED)

    organization = relationship("Organization")
    offices = relationship("Offices", back_populates="shifts")
    attendances = relationship("Attendance", back_populates="shift")


    # VALIDATION

    def validate(self):
        if self.start_time == self.end_time:
            raise ValueError("Shift start and end time cannot be the same")

        if not (0 <= self.break_minutes <= 240):
            raise ValueError("Break minutes must be between 0 and 240")

        if not (0 <= self.grace_before_minutes <= 120):
            raise ValueError("Grace before must be 0–120 minutes")

        if not (0 <= self.grace_after_minutes <= 120):
            raise ValueError("Grace after must be 0–120 minutes")

        # Auto-detect night shift
        if self.start_time > self.end_time:
            self.shift_type = ShiftTypeEnum.night
        else:
            self.shift_type = ShiftTypeEnum.fixed


    # BUSINESS HELPERS


    def is_night_shift(self) -> bool:
        return self.start_time > self.end_time

    def duration_minutes(self) -> int:
        """
        Accurate shift duration (handles night shift correctly)
        """
        start = datetime.combine(datetime.today(), self.start_time)
        end = datetime.combine(datetime.today(), self.end_time)

        if self.is_night_shift():
            end += timedelta(days=1)

        return int((end - start).total_seconds() / 60)

    def get_grace_config(self) -> dict:
        """
        Clean config-only helper (not business logic)
        """
        return {
            "before": self.grace_before_minutes,
            "after": self.grace_after_minutes
        }