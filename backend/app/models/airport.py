from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database.db import Base


class Airport(Base):
    __tablename__ = "airports"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(3), unique=True, nullable=False, index=True)
    name = Column(String(150), nullable=False)
    city = Column(String(100), nullable=False)
    country = Column(String(100), nullable=False)
    timezone = Column(String(50), nullable=False, default="Asia/Kolkata")

    departing_flights = relationship(
        "Flight", back_populates="origin",
        foreign_keys="Flight.origin_airport_id"
    )
    arriving_flights = relationship(
        "Flight", back_populates="destination",
        foreign_keys="Flight.destination_airport_id"
    )
    based_crew = relationship("Crew", back_populates="base_airport")