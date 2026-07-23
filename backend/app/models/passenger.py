from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database.db import Base


class Passenger(Base):
    __tablename__ = "passengers"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(150), nullable=False)
    email = Column(String(255), nullable=True)
    phone = Column(String(20), nullable=True)
    passport_number = Column(String(20), unique=True, nullable=True)

    bookings = relationship("Booking", back_populates="passenger")