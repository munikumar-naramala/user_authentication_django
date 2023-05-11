import graphene
from graphene_django import DjangoObjectType
from ..models.user_account import UserAccount
from ..views.user_account import CreateUserAccountView
import json
from ..utilities.send_email import send_email



class UserAccountType(DjangoObjectType):
    class Meta:
        model = UserAccount
        fields = ('id', 'email', 'firstname', 'lastname')


class UserAccountQuery(graphene.ObjectType):
    user_accounts = graphene.List(UserAccountType)
    def resolve_user_accounts(root, info, **kwargs):
        return UserAccount.objects.all()


class CreateUserAccountMutation(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        firstname = graphene.String(required=True)
        lastname = graphene.String(required=True)

    user_account = graphene.Field(UserAccountType)

    def mutate(root, info, email, password, firstname, lastname):
        view = CreateUserAccountView()
        request = info.context
        request.POST = {'email': email, 'password': password, 'firstname': firstname, 'lastname': lastname}
        response = view.post(request)
        response_content = response.content.decode('utf-8')
        response_dict = json.loads(response_content)

        if response.status_code == 201 and 'user_account' in response_dict:
            user_account_dict = response_dict['user_account']
            user_account = UserAccount.objects.get(id=user_account_dict['id'])
            subject = "Test Registration Email"
            text_content = "This is a Registration test email message."
            html_content = "<p>This is a <strong>Registration test email</strong> message.</p>"
            send_email(email,subject,text_content,html_content)
            return CreateUserAccountMutation(user_account=user_account)
        else:
            errors = response_dict.get('errors')
            if errors:
                raise Exception(errors)
            else:
                raise Exception('Failed to create user account')



class Mutation(graphene.ObjectType):
    create_user_account = CreateUserAccountMutation.Field()


user_account_schema = graphene.Schema(query=UserAccountQuery, mutation=Mutation)
# import graphene
# from graphene_django import DjangoObjectType
# from ..models.user_account import UserAccount
#
#
# class UserAccountType(DjangoObjectType):
#     class Meta:
#         model = UserAccount
#         fields = ('id', 'email', 'firstname', 'lastname')
#
#
# class CreateUserAccountMutation(graphene.Mutation):
#     class Arguments:
#         email = graphene.String(required=True)
#         password = graphene.String(required=True)
#         firstname = graphene.String(required=True)
#         lastname = graphene.String(required=True)
#
#     user_account = graphene.Field(UserAccountType)
#
#     def mutate(root, info, email, password, firstname, lastname):
#         # Your implementation to create user account
#         user_account = UserAccount.objects.create(email=email, password=password, firstname=firstname,
#                                                   lastname=lastname)
#
#         return CreateUserAccountMutation(user_account=user_account)
#
#     user_account = graphene.Field(UserAccountType)
#
#     def resolve_user_account(root, info):
#         return root.user_account
#
#
# class UserAccountQuery(graphene.ObjectType):
#     user_accounts = graphene.List(UserAccountType)
#
#     def resolve_user_accounts(root, info, **kwargs):
#         return UserAccount.objects.all()
#
#
# class Mutation(graphene.ObjectType):
#     create_user_account = CreateUserAccountMutation.Field()
#
#
# user_account_schema = graphene.Schema(query=UserAccountQuery, mutation=Mutation)
