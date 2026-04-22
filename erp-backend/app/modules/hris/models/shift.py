from .library.dependencies import *


class Shift(Base):
    __tablename__ = "shift"

    # -------------------
    # Identity
    # -------------------
    id = Column(Integer, primary_key=True, index=True)

    office_id = Column(
        Integer,
        ForeignKey("office.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)

    # Optional grouping (useful later)
    shift_code = Column(String(50), nullable=True)

    # -------------------
    # Shift timing
    # -------------------
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)

    break_minutes = Column(Integer, default=0)

    # -------------------
    # Rules
    # -------------------
    is_night_shift = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)

    # -------------------
    # Relationships
    # -------------------
    office = relationship(
        "Office",
        back_populates="shifts"
    )

    attendances = relationship(
        "Attendance",
        back_populates="shift"
    )

    # -------------------
    # Audit
    # -------------------
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )

    # -------------------
    # VALIDATION
    # -------------------
    def validate(self):
        """
        Call in service layer before save.
        """

        if self.start_time == self.end_time:
            raise ValueError("Shift start and end time cannot be the same")

        if self.start_time > self.end_time:
            self.is_night_shift = True
        else:
            self.is_night_shift = False

        if self.break_minutes < 0:
            raise ValueError("Break minutes cannot be negative")

        if self.break_minutes > 240:
            raise ValueError("Break minutes too large")