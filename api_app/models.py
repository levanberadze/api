from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=100)
    engine_size = models.FloatField(default=2.0)
