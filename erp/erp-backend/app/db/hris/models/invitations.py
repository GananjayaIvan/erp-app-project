from .library.dependencies import *
from app.db.hris.enums.employment_status import EmploymentStatus


class Invitations(Base):
    __tablename__ = "invitations"

    id = Column(Integer, primary_key=True)

    email = Column(String, nullable=False, index=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)

    role = Column(String, default="member", nullable=False)

    token = Column(String, unique=True, nullable=False)

    expires_at = Column(DateTime, nullable=False)

    accepted_at = Column(DateTime, nullable=True)