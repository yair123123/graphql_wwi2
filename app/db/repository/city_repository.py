from typing import List

from returns.result import Success, Failure
from sqlalchemy.exc import SQLAlchemyError

from app.db.database import session_maker
from app.db.models.City import City


def insert_city(city:City):
    try:
        with session_maker() as session:
            session.add(city)
            session.commit()
            session.refresh(city)
            return Success(city)
    except SQLAlchemyError as e:
        return Failure(str(e))
def insert_many_cities(cities:List[City]):
    try:
        with session_maker() as session:
            session.add_all(cities)
            session.commit()
            return Success("All cities are inserted successfully")
    except SQLAlchemyError as e:
        return Failure(str(e))
