from sqlalchemy import Column, Integer, String, CheckConstraint
from sqlalchemy.orm import relationship

from app.database.db import Base


class Aircraft(Base):
    __tablename__ = "aircraft"

    id = Column(Integer, primary_key=True, index=True)
    registration = Column(String(12), unique=True, nullable=False, index=True)
    model = Column(String(60), nullable=False)
    capacity = Column(Integer, nullable=False)
    status = Column(String(20), nullable=False, default="active")

    flights = relationship("Flight", back_populates="aircraft")

    __table_args__ = (
        CheckConstraint("capacity > 0 AND capacity <= 900",
                        name="aircraft_capacity_positive"),
        CheckConstraint("status IN ('active', 'maintenance', 'retired')",
                        name="aircraft_status_valid"),
    )