import graphene
from .country_timezone import TimezoneQuery, CreateTimezone
from .health_check import HealthQuery
from .organizations import CreateOrganizationMutation, OrgQuery
from .user_account import CreateUserAccountMutation, UserAccountQuery
from .user_verification import SendEmailMutation
from .forgot_password import ForgotPasswordMutation


class Query(TimezoneQuery, HealthQuery, OrgQuery, UserAccountQuery, graphene.ObjectType):
    pass


class Mutation(CreateTimezone, CreateOrganizationMutation, CreateUserAccountMutation, SendEmailMutation,
               ForgotPasswordMutation,
               graphene.ObjectType):
    create_timezone = CreateTimezone.Field()
    create_organization = CreateOrganizationMutation.Field()
    create_user_account = CreateUserAccountMutation.Field()
    user_verification = SendEmailMutation.Field()
    forgot_password = ForgotPasswordMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
