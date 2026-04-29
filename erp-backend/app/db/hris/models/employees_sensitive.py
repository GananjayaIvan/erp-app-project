from .library.dependencies import *
class EmployeeSensitive(Base):
    __tablename__ = "employee_sensitive"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"), unique=True)

    marital_status = Column(String)
    number_of_children = Column(Integer)

    # Identity (should be encrypted in production)
    identity_id = Column(String)
    tax_id = Column(String)
    social_security_id = Column(String)

    # Personal
    address = Column(String)
    date_of_birth = Column(DateTime)
    phone = Column(String)
    gender = Column(String)

    # Emergency
    emergency_contact_name = Column(String)
    emergency_contact_phone = Column(String)

    created_at = Column(DateTime, server_default=func.now())

    employee = relationship("Employee", back_populates="sensitive")
    __tablename__ = "employee_sensitive"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"), unique=True)

    marital_status = Column(String, index=True)

    number_of_children = Column(Integer, index=True)

    # Identity
    identity_id = Column(String, index=True)
    tax_id = Column(String, index=True)
    social_security_id = Column(String, index=True)     

    # Personal
    address = Column(String, nullable=True)
    date_of_birth = Column(DateTime, nullable=True)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, nullable=True)
    gender = Column(String, nullable=True)


    # Emergency
    emergency_contact_name = Column(String, nullable=True)
    emergency_contact_phone = Column(String, nullable=True)

    created_at = Column(DateTime, server_default=func.now())

    employee = relationship("Employees", back_populates="sensitive")