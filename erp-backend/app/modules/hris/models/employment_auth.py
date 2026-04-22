from .library.dependencies import *


class EmployeeAuth(Base):
    __tablename__ = "employee_auth"

    # -------------------
    # Identity
    # -------------------
    id = Column(Integer, primary_key=True)

    employee_id = Column(
        Integer,
        ForeignKey("employee.id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
        index=True
    )

    # IMPORTANT: use back_populates only (no backref conflict)
    employee = relationship(
        "Employee",
        back_populates="auth",
        uselist=False
    )

    # -------------------
    # Authentication
    # -------------------
    password_hash = Column(String, nullable=False)

    is_active = Column(Boolean, default=True, index=True)
    is_verified = Column(Boolean, default=False)

    # -------------------
    # Security tracking
    # -------------------
    failed_login_attempts = Column(Integer, default=0)

    locked_until = Column(DateTime, nullable=True, index=True)

    last_login_at = Column(DateTime, nullable=True)

    # -------------------
    # Password reset
    # -------------------
    reset_token = Column(String, nullable=True, index=True)

    reset_token_expiry = Column(DateTime, nullable=True)

    # -------------------
    # Audit
    # -------------------
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())