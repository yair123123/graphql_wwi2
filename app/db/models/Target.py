from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.models import Base
class Target(Base):
    __tablename__ = 'targets'
    target_id = Column(Integer, autoincrement=True, primary_key=True)
    mission_id = Column(Integer,ForeignKey("missions.mission_id"))
    target_industry = Column(String, nullable=False)
    city_id = Column(Integer, ForeignKey('cities.city_id'), nullable=False)
    target_type_id = Column(Integer, ForeignKey('targettypes.target_type_id'), nullable=True)
    target_priority = Column(Integer, nullable=True)

    city = relationship("City",back_populates="targets")
    target_type = relationship("TargetType")
    mission = relationship("Mission",back_populates="targets")