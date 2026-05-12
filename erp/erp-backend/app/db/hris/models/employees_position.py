from .library.dependencies import *


class EmployeesPosition(Base):
    __tablename__ = "employees_position"


    # IDENTITY

    id = Column(Integer, primary_key=True, index=True)


    # ORG CONTEXT (OPTIONAL BUT RECOMMENDED)

    organization_id = Column(
        Integer,
        ForeignKey("organizations.id", ondelete="CASCADE"),
        nullable=True,
        index=True
    )


    # POSITION DATA

    name = Column(String, nullable=False)

    description = Column(String, nullable=True)

    level = Column(String, nullable=True)  # e.g. junior, mid, senior, lead

    # Optional classification
    is_active = Column(Boolean, default=True, index=True)


    # AUDIT

    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )


    # RELATIONSHIPS (OPTIONAL)


    # If you want reverse access:
    employments = relationship(
        "EmploymentModel",
        back_populates="position",
        cascade="all"
    )