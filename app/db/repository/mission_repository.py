from returns.result import Success, Failure, Result
from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError

from app.db.database import session_maker
from app.db.models import Target
from app.db.models.Mission import Mission


def insert_mission(mission: Mission):

    try:
        with session_maker() as session:
            mission.mission_id = mission_id = session.query(func.max(Mission.mission_id)).scalar() + 1
            session.add(mission)
            session.commit()
            session.refresh(mission)
            return Success(mission)
    except SQLAlchemyError as e:
        return Failure(str(e))


def update_mission(mission: Mission):
    with session_maker() as session:
        try:
            mission = get_mission_by_id(mission.mission_id)
            if mission is None:
                return Failure(f"customer by id {id} not found")
            mission_to_update = session.merge(mission)
            mission_to_update.airborne_aircraft = mission.airborne_aircraft
            mission_to_update.aircraft_returned = mission.aircraft_returned
            mission_to_update.attacking_aircraft = mission.attacking_aircraft
            mission_to_update.aircraft_failed = mission.aircraft_failed
            mission_to_update.aircraft_lost = mission.aircraft_lost
            session.commit()
            session.refresh(mission_to_update)
            return Success(mission_to_update)
        except SQLAlchemyError as e:
            session.rollback()
            Failure(str(e))

def delete_mission(mission_id:int) -> Result[str,str]:
    mission = get_mission_by_id(mission_id)
    if not mission:
        return Failure("not found")
    try:
        with session_maker() as session:
            session.delete(mission)
            session.commit()
            return Success("the mission is deleted successfully")
    except SQLAlchemyError as e:
        return Failure(str(e))
def get_mission_by_id(mission_id: int):
    with session_maker() as session:
        return session.get(Mission, mission_id)


def get_missions_by_range_date(start, end):
    with session_maker() as session:
        return session.query(Mission).filter((Mission.mission_date > start) & (Mission.mission_date < end)).all()


def get_missions_by_country(country_name: str):
    with session_maker() as session:
        return session.query(Mission).filter(Mission.target.city.country == country_name).all()

def get_mission_by_target_industry(target_industry: str):
    with session_maker() as session:
        missions = session.query(Mission).join(Mission.target).filter(Target.target_industry == target_industry).all()
        return missions

def get_air_crafts_by_mission(mission_id: int):
    with session_maker() as session:
        return session.query(Mission).with_entities(Mission.attacking_aircraft).get(mission_id)


def get_result_attack_by_target_type_name(target_type_name):
    with session_maker() as session:
        return session.query(Mission).join(Mission.target).join(Target.target_type).filter(TargetType.target_type_name == target_type_name).all()
