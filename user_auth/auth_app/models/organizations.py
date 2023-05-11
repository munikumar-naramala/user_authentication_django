from django.db import models
import uuid


class Organizations(models.Model):
    objects = None
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=250)
    description = models.TextField()
    address = models.TextField()

    class Meta:
        db_table = 'organizations'
