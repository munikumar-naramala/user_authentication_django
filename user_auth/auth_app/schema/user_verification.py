import graphene
from ..utilities.send_email import send_email


class SendEmailMutation(graphene.Mutation):
    class Arguments:
        to_email = graphene.String(required=True)

    success = graphene.Boolean()

    def mutate(self, info, to_email):
        subject = "Test Registration Email"
        text_content = "This is a Registration test email message."
        html_content = "<p>This is a <strong>Registration test email</strong> message.</p>"
        send_email(to_email, subject, text_content, html_content)
        return SendEmailMutation(success=True)


class Mutation(graphene.ObjectType):
    send_email = SendEmailMutation.Field()


verification_schema = graphene.Schema(mutation=Mutation)
