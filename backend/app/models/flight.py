from sqlalchemy import (
    Column, Integer, String, DateTime, ForeignKey,
    CheckConstraint, UniqueConstraint
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.db import Base


class Flight(Base):
    __tablename__ = "flights"

    id = Column(Integer, primary_key=True, index=True)
    flight_number = Column(String(10), nullable=False, index=True)

    aircraft_id = Column(
        Integer, ForeignKey("aircraft.id", ondelete="RESTRICT"),
        nullable=False, index=True
    )
    origin_airport_id = Column(
        Integer, ForeignKey("airports.id", ondelete="RESTRICT"),
        nullable=False, index=True
    )
    destination_airport_id = Column(
        Integer, ForeignKey("airports.id", ondelete="RESTRICT"),
        nullable=False, index=True
    )

    scheduled_departure = Column(DateTime(timezone=True), nullable=False, index=True)
    scheduled_arrival = Column(DateTime(timezone=True), nullable=False)
    actual_departure = Column(DateTime(timezone=True), nullable=True)
    actual_arrival = Column(DateTime(timezone=True), nullable=True)

    status = Column(String(20), nullable=False, default="scheduled", index=True)
    gate = Column(String(10), nullable=True)
    delay_minutes = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    aircraft = relationship("Aircraft", back_populates="flights")
    origin = relationship(
        "Airport", back_populates="departing_flights",
        foreign_keys=[origin_airport_id]
    )
    destination = relationship(
        "Airport", back_populates="arriving_flights",
        foreign_keys=[destination_airport_id]
    )
    crew_assignments = relationship(
        "CrewAssignment", back_populates="flight",
        cascade="all, delete-orphan"
    )
    bookings = relationship(
        "Booking", back_populates="flight",
        cascade="all, delete-orphan"
    )

    __table_args__ = (
        CheckConstraint(
            "status IN ('scheduled','boarding','departed','in_air',"
            "'landed','delayed','cancelled')",
            name="flights_status_valid"),
        CheckConstraint("scheduled_arrival > scheduled_departure",
                        name="flights_arrival_after_departure"),
        CheckConstraint("origin_airport_id <> destination_airport_id",
                        name="flights_origin_not_destination"),
        CheckConstraint("delay_minutes >= 0",
                        name="flights_delay_not_negative"),
        UniqueConstraint("flight_number", "scheduled_departure",
                         name="flights_number_departure_unique"),
    )