from .library.dependencies import *



class ShiftTypeEnum(str, PyEnum):
    fixed = "fixed"
    shift = "shift"
    flexible = "flexible"
    full_24_7 = "24_7"


class OfficePolicy(Base):
    __tablename__ = "office_policy"

    id = Column(Integer, primary_key=True)

    office_id = Column(
        Integer,
        ForeignKey("office.id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
        index=True
    )

    office = relationship(
        "Office",
        back_populates="policy",
        uselist=False
    )

    working_days = Column(JSON, nullable=False)

    working_hours_start = Column(Time, nullable=True)
    working_hours_end = Column(Time, nullable=True)

    shift_type = Column(
        SQLEnum(ShiftTypeEnum, name="shift_type_enum"),
        nullable=False,
        default=ShiftTypeEnum.fixed
    )

    late_grace_minutes = Column(Integer, default=10)
    overtime_enabled = Column(Boolean, default=True)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    def validate(self):
        allowed_days = {"mon", "tue", "wed", "thu", "fri", "sat", "sun"}

        if not self.working_days:
            raise ValueError("working_days cannot be empty")

        invalid_days = set(self.working_days) - allowed_days
        if invalid_days:
            raise ValueError(f"Invalid working days: {invalid_days}")

        if self.working_hours_start and self.working_hours_end:
            if self.working_hours_start >= self.working_hours_end:
                raise ValueError("Start time must be before end time")

        if self.shift_type == ShiftTypeEnum.full_24_7:
            return

        if self.shift_type == ShiftTypeEnum.fixed:
            if not self.working_days:
                raise ValueError("Fixed shift must define working days")