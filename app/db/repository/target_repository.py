from returns.result import Result, Success, Failure
from sqlalchemy.exc import SQLAlchemyError

from app.db.database import session_maker
from app.db.models import Target


def insert_target(target:Target) -> Result[Target,str]:
    try:
        with session_maker() as session:
            session.add(target)
            session.commit()
            session.refresh(target)
            return Success(target)
    except SQLAlchemyError as e:
        return Failure(str(e))

