import uuid
from django.db import models


class UserAccount(models.Model):
    objects = None
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    password = models.CharField(max_length=225, null=False, default='password')
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)

    class Meta:
        db_table = 'user-account'

    def __str__(self):
        return self.email
