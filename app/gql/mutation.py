from graphene import Mutation, InputObjectType, Date, Float, Field, ObjectType, Int, String, Boolean
from returns.result import Success
from sqlalchemy import false

from app.db.models import Mission, Target
from app.db.repository.mission_repository import insert_mission, update_mission, delete_mission
from app.db.repository.target_repository import insert_target
from app.gql.query import Query
from app.gql.types.MissionType import MissionType
from app.gql.types.TargetType import TargetType


class TargetInput(InputObjectType):
    mission_id = Int()
    target_industry = String()
    city_id = Int()
    target_type_id = Int()
    target_priority = Int()


class MissionInput(InputObjectType):
    mission_date = Date()
    airborne_aircraft = Float()
    attacking_aircraft = Float()
    aircraft_returned = Float()
    aircraft_failed = Float()
    aircraft_lost = Float()


class ResultMissionInput(InputObjectType):
    airborne_aircraft = Float()
    attacking_aircraft = Float()
    aircraft_returned = Float()
    aircraft_failed = Float()
    aircraft_lost = Float()


class CreateMission(Mutation):
    class Arguments:
        missionInput = MissionInput()

    mission = Field(MissionType)

    @staticmethod
    def mutate(root, info, missionInput):
        return CreateMission(mission=Query.check_response(insert_mission(Mission(**missionInput))))


class CreateTarget(Mutation):
    class Arguments:
        target_input = TargetInput()

    target = Field(TargetType)

    @staticmethod
    def mutate(root, info, target_input):
        return CreateTarget(Query.check_response(insert_target(Target(**target_input))))


class UpdateResultMission(Mutation):
    class Arguments:
        mission_input = ResultMissionInput()

    mission = Field(MissionType)

    @staticmethod
    def mutate(root, info, mission_input):
        return UpdateResultMission(mission=Query.check_response(update_mission(mission_input)))


class DeleteMission(Mutation):
    class Arguments:
        mission_id = Int()

    result= Field(Boolean)
    message = Field(String)
    @staticmethod
    def mutate(root,info,mission_id):
        result = delete_mission(mission_id)

        return DeleteMission(result= True if isinstance(result,Success) else False ,message=str(result))


class Mutations(ObjectType):
    insert_mission = CreateMission.Field()
    insert_target = CreateTarget.Field()
    update_result_mission = UpdateResultMission.Field()
    delete_mission = DeleteMission.Field()
