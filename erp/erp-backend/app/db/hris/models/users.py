from .library.dependencies import *

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    authentik_id = Column(String, unique=True, index=True)

    email = Column(String, unique=True)
    created_at = Column(DateTime, server_default=func.now())