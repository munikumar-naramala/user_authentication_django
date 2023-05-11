import uuid
from django.db import models
from .organizations import Organizations


class Roles(models.Model):
    objects = None
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250)
    description = models.TextField()
    created_by = models.UUIDField()
    last_modified_by = models.UUIDField()
    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    gt_date_added = models.DateTimeField(auto_now_add=True)
    gt_last_modified = models.DateTimeField(auto_now=True)
    ip_address = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    code = models.CharField(max_length=50)
    default_role = models.BooleanField(default=True)
    all_devices = models.BooleanField(default=True)

    class Meta:
        db_table = 'roles'

    def __str__(self):
        return self.name

