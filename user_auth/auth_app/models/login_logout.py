import uuid
from django.db import models
from .user_account import UserAccount


class LoginLogout(models.Model):
    objects = None
    login_logout_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    token = models.TextField()
    login_time = models.DateTimeField(auto_now_add=True)
    logout_time = models.DateTimeField(null=True, default=None)

    class Meta:
        db_table = 'login-logout'
