from app.db.database import session_maker
from app.db.models import Mission, Target, City


def get_mission_by_city(city_name_query):
    try:
        with session_maker() as session:
            missions = (
                session.query(Mission)
                .join(Mission.target)
                .join(Target.city)
                .filter(Target.city_name == city_name_query)
                .all()
            )
            return missions if missions else []
    except Exception as e:
        print(f"Error fetching missions for city {city_name_query}: {e}")
        return []

print(get_mission_by_city("18 03 N 120 3"))