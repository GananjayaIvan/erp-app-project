from .library.dependencies import *


class User(Base):
    __tablename__ = "users"

    __table_args__ = {"schema": "hris"}

    id = Column(Integer, primary_key=True)

    zitadel_id = Column(
        String,
        unique=True,
        index=True,
        nullable=False
    )

    employee_id = Column(
        Integer,
        ForeignKey("hris.employees.id"),
        nullable=True,
        unique=True
    )

    email = Column(
        String,
        unique=True,
        nullable=False
    )

    created_at = Column(
        DateTime,
        server_default=func.now()
    )

    # AUTH
    employee = relationship(
        "Employees",
        back_populates="user",
        uselist=False
    )