from app.stats.stat_repositoty import get_mission_by_city


def stat_mission_by_city(city_name: str):
    missions = get_mission_by_city(city_name)

    count_of_missions = len(missions)
    if count_of_missions == 0:
        return 0
    sum_priorities = sum(mission["target"]["target_priority"] for mission in missions)
    average = sum_priorities / count_of_missions
    result = {
        "counts_of_missions":count_of_missions,
    "average_priority":average
    }
    return result