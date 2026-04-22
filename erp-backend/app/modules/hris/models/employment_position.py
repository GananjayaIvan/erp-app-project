from .library.dependencies import *

class EmployeePosition(Base):
    __tablename__ = "employee_position"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    employee_id = Column(Integer, ForeignKey("employee.id"), nullable=False)

    employees = relationship("Employee", back_populates="position")