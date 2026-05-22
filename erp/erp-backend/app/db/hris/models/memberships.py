from .library.dependencies import *
from sqlalchemy import Enum as SQLEnum, UniqueConstraint
from app.db.hris.enums.membership import MembershipRole


class Membership(Base):
    __tablename__ = "memberships"

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "organization_id",
            name="uq_user_org"
        ),
        {"schema": "hris"}
    )

    id = Column(Integer, primary_key=True)

    # RELATIONS

    user_id = Column(
        Integer,
        ForeignKey("hris.users.id"),
        nullable=False,
        index=True
    )

    organization_id = Column(
        Integer,
        ForeignKey("hris.organizations.id"),
        nullable=False,
        index=True
    )

    # ROLE IN ORG

    role = Column(
        SQLEnum(
            MembershipRole,
            name="membership_role_enum"
        ),
        default=MembershipRole.MEMBER,
        nullable=False,
        index=True
    )

    # INVITE / AUDIT TRACKING

    invited_by_id = Column(
        Integer,
        ForeignKey("hris.users.id"),
        nullable=True
    )

    # LIFECYCLE

    joined_at = Column(
        DateTime,
        server_default=func.now(),
        nullable=False
    )

    left_at = Column(DateTime, nullable=True)

    is_active = Column(
        Boolean,
        default=True,
        index=True
    )

    # RELATIONSHIPS

    user = relationship(
        "User",
        foreign_keys=[user_id]
    )

    organization = relationship(
        "Organization",
        foreign_keys=[organization_id]
    )

    invited_by = relationship(
        "User",
        foreign_keys=[invited_by_id]
    )