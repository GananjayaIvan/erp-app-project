from .library.dependencies import *

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)

    is_active = Column(Boolean, default=True, index=True)
    verified_at = Column(DateTime, nullable=True)

    failed_login_attempts = Column(Integer, default=0, nullable=False)
    locked_until = Column(DateTime, nullable=True, index=True)
    last_login_at = Column(DateTime, nullable=True)

    password_changed_at = Column(DateTime, nullable=True)

    reset_token_hash = Column(String, nullable=True, index=True)
    reset_token_expiry = Column(DateTime, nullable=True, index=True)

    deleted_at = Column(DateTime, nullable=True, index=True)

    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )