from .library.dependencies import *

class User(Base):
    __tablename__ = "users"

    # IDENTITY
    id = Column(Integer, primary_key=True)

    email = Column(String, unique=True, index=True, nullable=False)

    password_hash = Column(String(255), nullable=False)

    # STATUS
    is_active = Column(Boolean, default=True, index=True)

    is_verified = Column(Boolean, default=False)

    # SECURITY TRACKING
    failed_login_attempts = Column(Integer, default=0, nullable=False)

    locked_until = Column(DateTime, nullable=True, index=True)

    last_login_at = Column(DateTime, nullable=True)

    # PASSWORD RESET
    reset_token_hash = Column(String, nullable=True, index=True)

    reset_token_expiry = Column(DateTime, nullable=True, index=True)

    # AUDIT
    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

    # BUSINESS LOGIC

    def is_locked(self):
        return self.locked_until is not None and self.locked_until > func.now()

    def reset_failed_attempts(self):
        self.failed_login_attempts = 0
        self.locked_until = None

    def increment_failed_attempts(self, max_attempts: int = 5):
        self.failed_login_attempts += 1

        if self.failed_login_attempts >= max_attempts:
            self.locked_until = func.now() + timedelta(minutes=15)

    def mark_login_success(self):
        self.last_login_at = func.now()
        self.reset_failed_attempts()