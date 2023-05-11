from django.core.mail import EmailMultiAlternatives, get_connection
from django.conf import settings
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "email-smtp.us-east-1.amazonaws.com"
EMAIL_HOST_USER = "AKIAWFR6GNHNLLDBJ7CM"
EMAIL_HOST_PASSWORD = "BEJN3J+bzm14Ch9mUniQ/XUc8kUhZC5R2RHcizzo3Awo"
EMAIL_USE_TLS = True
EMAIL_SENDER = "NetSec <no-reply@veritasweaver.io>"
# settings.configure()


def send_email(to_email, subject, text_content, html_content):

    try:
        connection = get_connection(
            backend=EMAIL_BACKEND,
            username=EMAIL_HOST_USER,
            password=EMAIL_HOST_PASSWORD,
            host=EMAIL_HOST,
            use_tls=EMAIL_USE_TLS
        )
        connection.open()
        email = EmailMultiAlternatives(
            subject=subject,
            body=text_content,
            from_email=EMAIL_SENDER,
            to=[to_email],
            connection=connection
        )
        email.attach_alternative(html_content, "text/html")
        email.send()
        print("Email sent successfully!")
    except Exception as e:
        print("Email sending failed. Error: ", str(e))
    finally:
        get_connection().close()


# if __name__ == '__main__':
#     #to_email = input("Enter the recipient email address: ")
#     to_email = 'nmunikumar@gmail.com'
#     subject = "Test Email"
#     text_content = "This is a test email message."
#     html_content = "<p>This is a <strong>test email</strong> message.</p>"
#
#     send_email(to_email, subject, text_content, html_content)
