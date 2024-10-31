from graphene import ObjectType, Int, String, Field

from app.gql.types.MissionType import MissionType


class TargetType(ObjectType):
    target_id = Int()
    mission_id = Int()
    target_industry = String()
    city_id = Int()
    target_type_id = Int()
    target_priority = Int()

    mission = Field(MissionType)