
from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.orm import relationship

from app.db.models import Base


class Mission(Base):
    __tablename__ = "missions"

    mission_id = Column(Integer, primary_key=True, autoincrement=True)
    mission_date = Column(Date, nullable=False)
    airborne_aircraft = Column(Float,nullable=True)
    attacking_aircraft = Column(Float,nullable=True)
    aircraft_returned = Column(Float,nullable=True)
    aircraft_failed = Column(Float,nullable=True)
    aircraft_lost = Column(Float,nullable=True)


    target = relationship("Target",back_populates="mission",lazy="joined")

