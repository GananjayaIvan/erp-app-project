from .library.dependencies import *


class Attendance(Base):
    __tablename__ = "attendance"


    # Identity

    id = Column(Integer, primary_key=True, index=True)

    employee_id = Column(
        Integer,
        ForeignKey("employee.id"),
        nullable=False,
        index=True
    )

    # Link to shift
    shift_id = Column(
        Integer,
        ForeignKey("shift.id"),
        nullable=True,
        index=True
    )


    # Time tracking

    checkin = Column(DateTime(timezone=True), server_default=func.now())
    checkout = Column(DateTime(timezone=True), nullable=True)

    # Computed/Stored duration (optional but useful)
    worked_minutes = Column(Integer, nullable=True)


    # Status

    status = Column(
        String(20),
        default="present"
    )
    # present | late | absent | half_day | overtime


    # Relationships

    employee = relationship("Employee", back_populates="attendances")

    shift = relationship("Shift", backref="attendances")


    # Audit

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )


    # BUSINESS LOGIC

    def calculate_worked_time(self):
        """
        Calculate worked minutes (call in service layer ideally)
        """
        if self.checkin and self.checkout:
            delta = self.checkout - self.checkin
            self.worked_minutes = int(delta.total_seconds() / 60)
        else:
            self.worked_minutes = None