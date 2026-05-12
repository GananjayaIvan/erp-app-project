from .library.dependencies import *
from app.db.hris.enums.attendance import *
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
