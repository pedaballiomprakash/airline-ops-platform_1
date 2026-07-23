from sqlalchemy import (
    Column, Integer, String, DateTime, ForeignKey,
    CheckConstraint, UniqueConstraint
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.db import Base


class CrewAssignment(Base):
    __tablename__ = "crew_assignments"

    id = Column(Integer, primary_key=True, index=True)
    flight_id = Column(
        Integer, ForeignKey("flights.id", ondelete="CASCADE"),
        nullable=False, index=True
    )
    crew_id = Column(
        Integer, ForeignKey("crew.id", ondelete="RESTRICT"),
        nullable=False, index=True
    )
    role_on_flight = Column(String(30), nullable=False)
    assigned_at = Column(DateTime(timezone=True), server_default=func.now())

    flight = relationship("Flight", back_populates="crew_assignments")
    crew = relationship("Crew", back_populates="assignments")

    __table_args__ = (
        CheckConstraint(
            "role_on_flight IN ('captain', 'first_officer', 'cabin_crew')",
            name="crew_assignments_role_valid"),
        UniqueConstraint("flight_id", "crew_id",
                         name="crew_assignments_unique"),
    )