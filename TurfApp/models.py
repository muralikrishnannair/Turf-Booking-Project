
from django.db import models


class TurfDb(models.Model):

    turf_name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

    turf_type = models.CharField(max_length=100)

    price_per_hour = models.PositiveIntegerField()

    available = models.BooleanField(default=True)

    def __str__(self):
        return self.turf_name