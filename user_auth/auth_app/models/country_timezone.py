from django.db import models


class Timezone(models.Model):
    objects = None
    country = models.TextField(max_length=100)
    timezone = models.TextField(max_length=200)

    class Meta:
        db_table = 'country-timezone'

    def __str__(self):
        return self.country
