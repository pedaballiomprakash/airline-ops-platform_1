from sqlalchemy import Column, Integer, String, Date, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship

from app.database.db import Base


class Crew(Base):
    __tablename__ = "crew"

    id = Column(Integer, primary_key=True, index=True)
    employee_code = Column(String(20), unique=True, nullable=False, index=True)
    full_name = Column(String(150), nullable=False)
    role = Column(String(30), nullable=False)
    license_expiry = Column(Date, nullable=True)
    base_airport_id = Column(
        Integer, ForeignKey("airports.id", ondelete="RESTRICT"),
        nullable=False, index=True
    )
    status = Column(String(20), nullable=False, default="available")

    base_airport = relationship("Airport", back_populates="based_crew")
    assignments = relationship("CrewAssignment", back_populates="crew")

    __table_args__ = (
        CheckConstraint("role IN ('captain', 'first_officer', 'cabin_crew')",
                        name="crew_role_valid"),
        CheckConstraint(
            "status IN ('available', 'on_duty', 'rest', 'unavailable')",
            name="crew_status_valid"),
    )