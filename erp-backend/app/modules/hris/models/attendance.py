from .library.dependencies import *
from app.modules.hris.enums.attendance import *

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)

    organization_id = Column(
        Integer,
        ForeignKey("organizations.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    employees_id = Column(
        Integer,
        ForeignKey("employees.id"),
        nullable=False,
        index=True
    )

    shift_id = Column(
        Integer,
        ForeignKey("shift.id"),
        nullable=True,
        index=True
    )

    # Time tracking
    checkin = Column(DateTime(timezone=True), server_default=func.now())
    checkout = Column(DateTime(timezone=True), nullable=True)
    worked_minutes = Column(Integer, nullable=True)

    status = Column(String(20), default="present")

    # Relationships
    employees = relationship("Employees", back_populates="attendances")
    shift = relationship("Shift", backref="attendances")
    organization = relationship("Organization")

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