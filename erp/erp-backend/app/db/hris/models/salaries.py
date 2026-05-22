from .library.dependencies import *


class Salaries(Base):
    __tablename__ = "salaries"

    __table_args__ = {"schema": "hris"}

    
    # IDENTITY
    
    id = Column(Integer, primary_key=True, index=True)

    
    # ORG CONTEXT
    
    organization_id = Column(
        Integer,
        ForeignKey("hris.organizations.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    
    # CORE RELATION (IMPORTANT)
    
    employment_id = Column(
        Integer,
        ForeignKey("hris.employment_models.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    
    # PAYROLL DATA
    
    amount = Column(Integer, nullable=False)

    currency = Column(String, default="IDR")

    # Optional: salary type
    bonus = Column(Integer, nullable=True)
    allowance = Column(Integer, nullable=True)

    
    # TIMELINE (VERY IMPORTANT)
    
    effective_from = Column(DateTime, nullable=False)
    effective_to = Column(DateTime, nullable=True)

    
    # AUDIT
    
    created_at = Column(DateTime, server_default=func.now())

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )

    
    # RELATIONSHIPS
    
    employment = relationship("EmploymentModel")
    organization = relationship("Organization")