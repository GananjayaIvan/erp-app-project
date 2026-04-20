from sqlalchemy import Column, Integer, String, Date, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.core.database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)
    email = Column(String, unique=True)
    phone = Column(String)

    branch_id = Column(Integer, ForeignKey("branches.id"), nullable=False)
    position_id = Column(Integer, ForeignKey("positions.id"))

    hire_date = Column(Date)
    is_active = Column(Boolean, default=True)

    # relationships
    branch = relationship("Branch")
    position = relationship("Position")