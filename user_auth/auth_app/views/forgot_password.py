import json

from django.http import JsonResponse
from django.views import View

from ..models import UserAccount
from ..utilities.send_email import EMAIL_SENDER, send_email


class ForgotPasswordView(View):
    def post(self, request, *args, **kwargs):
        payload = json.loads(request.body)
        email = payload.get('email')

        try:
            user = UserAccount.objects.get(email=email)
        except UserAccount.DoesNotExist:
            return JsonResponse({'message': 'User does not exist'}, status=400)

        reset_password_link = self.generate_reset_password_link(user)
        self.send_reset_password_email(user.email, reset_password_link)

        response_data = {
            'reset_password_link': reset_password_link
        }

        return JsonResponse(response_data)

    @staticmethod
    def generate_reset_password_link(user):
        # Generate the reset password link here
        reset_password_link = "https://example.com/reset-password"
        return reset_password_link

    @staticmethod
    def send_reset_password_email(email, reset_password_link):
        # Send the reset password email
        subject = "Reset Password"
        message = f"Click the following link to reset your password: {reset_password_link}"
        send_email(subject, message, EMAIL_SENDER, [email])
