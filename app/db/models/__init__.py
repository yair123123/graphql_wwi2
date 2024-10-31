from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
from .Mission import Mission
from .Country import Country
from .City import City
from .Target_type import TargetType
from .Target import Target