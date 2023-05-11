import graphene
from graphene_django import DjangoObjectType
from ..models.organizations import Organizations
from ..views.organizations import CreateOrganizationView, ListOrganizationsView
import json


class OrganizationType(DjangoObjectType):
    class Meta:
        model = Organizations
        fields = ('id', 'name', 'description', 'address')


class OrgQuery(graphene.ObjectType):
    all_organizations = graphene.List(OrganizationType)

    def resolve_all_organizations(root, info):
        return Organizations.objects.all()


class CreateOrganizationMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        address = graphene.String(required=True)

    organization = graphene.Field(OrganizationType)

    def mutate(self, info, name, description, address):
        view = CreateOrganizationView()
        request = info.context
        request._body = json.dumps({'name': name, 'description': description, 'address': address})
        response_data = view.post(request)
        organization = Organizations.objects.get(id=response_data.get('id'))
        return CreateOrganizationMutation(organization=organization)

class Query(graphene.ObjectType):
    organizations = graphene.List(OrganizationType)

    def resolve_organizations(self, info):
        return Organizations.objects.all()

class Mutation(graphene.ObjectType):
    create_organization = CreateOrganizationMutation.Field()


schema = graphene.Schema(query=OrgQuery, mutation=Mutation)
