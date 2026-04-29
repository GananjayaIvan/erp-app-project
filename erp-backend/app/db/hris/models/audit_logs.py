from .library.dependencies import *
from app.db.hris.enums.attendance import *

class AuditLogs(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)

    actor_user_id = Column(Integer, ForeignKey("users.id"))
    action = Column(String, nullable=False)
    entity = Column(String, nullable=False)
    entity_id = Column(Integer)

    created_at = Column(DateTime, server_default=func.now(), index=True)