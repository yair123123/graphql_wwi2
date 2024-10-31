

from sqlalchemy import Column, Integer,String

from app.db.models import Base


class TargetType(Base):
    __tablename__ = 'targettypes'
    target_type_id = Column(Integer, autoincrement=True, primary_key=True)
    target_type_name = Column(String(255), unique=True, nullable=False)