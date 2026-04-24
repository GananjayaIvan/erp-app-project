from .library.dependencies import *
from app.modules.hris.enums.employment_status import EmploymentStatus


class Membership(Base):
    __tablename__ = "memberships"

    id = Column(Integer, primary_key=True)

    user_id = Column(ForeignKey("users.id"), nullable=False)
    organization_id = Column(ForeignKey("organizations.id"), nullable=False)

    role = Column(String, nullable=False)