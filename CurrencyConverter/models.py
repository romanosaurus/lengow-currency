from django.db import models


class Cube(models.Model):
    currency = models.CharField(max_length=200)
    rate = models.FloatField()
