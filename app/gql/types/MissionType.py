from graphene import ObjectType, Int, Date, String, Float, Field



class MissionType(ObjectType):
    mission_id = Int()
    mission_date = Date()
    airborne_aircraft = Float()
    attacking_aircraft = Float()
    aircraft_returned = Float()
    aircraft_failed =Float()
    aircraft_lost = Float()
