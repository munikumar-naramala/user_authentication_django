import graphene


class HealthQuery(graphene.ObjectType):
    status = graphene.String()

    def resolve_status(self, info):
        return "Microservice is active"


health_schema = graphene.Schema(query=HealthQuery)
