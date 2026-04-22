from .library.dependencies import *

class Salary(Base):
    __tablename__ = "salary"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employee.id"), nullable=False)
    amount = Column(Integer, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    employee = relationship("Employee")