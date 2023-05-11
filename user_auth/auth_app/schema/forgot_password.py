import graphene
from graphene import String, Mutation
from ..views.forgot_password import ForgotPasswordView
import json
from ..utilities.send_email import send_email


class ForgotPasswordMutation(Mutation):
    reset_password_link = String()

    class Arguments:
        email = String(required=True)

    def mutate(self, info, email):
        # Call the ForgotPasswordView to initiate the forget password process
        view = ForgotPasswordView()
        request = info.context
        request._body = json.dumps({'email': email})
        response_data = view.post(request)
        reset_password_link = 'www.google.com'
        subject = "Forgot Password Test Email"
        text_content = reset_password_link

        html_content = "<p>This is a <strong>Forgot Password test email</strong> message.</p>"
        reset_password_link = 'www.google.com'
        send_email(email, subject, html_content, reset_password_link)

        return ForgotPasswordMutation(reset_password_link=reset_password_link)


class Mutation(graphene.ObjectType):
    forgot_password = ForgotPasswordMutation.Field()


schema = graphene.Schema(mutation=Mutation)
