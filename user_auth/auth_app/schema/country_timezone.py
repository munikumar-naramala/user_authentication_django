import graphene
from graphene_django import DjangoObjectType
from ..models.country_timezone import Timezone
from ..views.country_timezone import CreateTimezoneView, ListTimezoneView
import json


class TimezoneType(DjangoObjectType):
    class Meta:
        model = Timezone
        fields = ("id", "country", "timezone")


class TimezoneQuery(graphene.ObjectType):
    timezone = graphene.List(TimezoneType)

    def resolve_timezone(self, info, **kwargs):
        return Timezone.objects.all()


class CreateTimezone(graphene.Mutation):
    class Arguments:
        country = graphene.String()
        timezone = graphene.String()

    ok = graphene.Boolean()
    timezone = graphene.Field(TimezoneType)

    def mutate(self, info, country, timezone):
        view = CreateTimezoneView()
        request = info.context
        request._body = json.dumps({'country': country, 'timezone': timezone})
        response = view.post(request)
        response_content = json.loads(response.content)
        timezone = response_content.get('timezone')
        return CreateTimezone(ok=True, timezone=Timezone(id=timezone.get('id'), country=timezone.get('country'),
                                                         timezone=timezone.get('timezone')))


class Mutation(graphene.ObjectType):
    create_timezone = CreateTimezone.Field()


timezone_schema = graphene.Schema(query=TimezoneQuery, mutation=Mutation)

"""
--> GET: 
query{
  timezone{
    id
    country
    timezone
  }
}

--> POST:
mutation {
  createTimezone(country: "India", timezone: "IST") {
    ok
    timezone {
      id
      country
      timezone
    }
  }
}

"""
