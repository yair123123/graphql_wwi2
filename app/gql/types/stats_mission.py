from graphene import ObjectType, Int, Date, String, Float, Field



class StateMissionType(ObjectType):
    counts_of_missions = Int()
    average_priority = Float()