from sqlalchemy import (
    Column, Integer, String, Numeric, DateTime, ForeignKey,
    CheckConstraint, UniqueConstraint
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.db import Base


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    booking_reference = Column(String(6), unique=True, nullable=False, index=True)
    flight_id = Column(
        Integer, ForeignKey("flights.id", ondelete="CASCADE"),
        nullable=False, index=True
    )
    passenger_id = Column(
        Integer, ForeignKey("passengers.id", ondelete="RESTRICT"),
        nullable=False, index=True
    )
    seat_number = Column(String(4), nullable=True)
    booking_status = Column(String(20), nullable=False, default="confirmed")
    fare_amount = Column(Numeric(10, 2), nullable=True)
    baggage_count = Column(Integer, nullable=False, default=0)
    booked_at = Column(DateTime(timezone=True), server_default=func.now())

    flight = relationship("Flight", back_populates="bookings")
    passenger = relationship("Passenger", back_populates="bookings")

    __table_args__ = (
        CheckConstraint(
            "booking_status IN ('confirmed','checked_in','boarded',"
            "'cancelled','no_show')",
            name="bookings_status_valid"),
        CheckConstraint("fare_amount >= 0", name="bookings_fare_not_negative"),
        CheckConstraint("baggage_count >= 0", name="bookings_baggage_not_negative"),
        UniqueConstraint("flight_id", "seat_number", name="bookings_seat_unique"),
    )