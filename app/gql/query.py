from graphene import ObjectType, List, Int, Field, Date, String
from graphql import GraphQLError
from returns.result import Result, Success

from app.db.repository.mission_repository import get_mission_by_id, get_missions_by_range_date, get_missions_by_country, \
    get_mission_by_target_industry, get_result_attack_by_target_type_name
from app.gql.types.MissionType import MissionType


class Query(ObjectType):
    @staticmethod
    def check_response(response):
        result:Result = response
        if isinstance(result,Success):
            return result.unwrap()
        else:
            raise GraphQLError(str(result))
    mission_by_id = Field(MissionType,mission_id = Int())
    missions_by_range_date = List(MissionType,start=Date(), end=Date())
    missions_by_country = List(MissionType,country_name=String())
    mission_by_target_industry=List(MissionType,target_industry=String())
    attack_by_target_type_name=List(MissionType,target_type_name=String())
    @staticmethod
    def resolve_mission_by_id(root,info,mission_id):
        return get_mission_by_id(mission_id)
    @staticmethod
    def resolve_missions_by_range_date(root,info,start,end):
        return get_missions_by_range_date(start,end)
    @staticmethod
    def resolve_missions_by_country(root,info,country_name):
        return get_missions_by_country(country_name)
    @staticmethod
    def resolve_mission_by_target_industry(root,info,target_industry):
        return get_mission_by_target_industry(target_industry)
    @staticmethod
    def resolve_attack_by_target_type_name(root,info,target_type_name):
        return get_result_attack_by_target_type_name(target_type_name)
