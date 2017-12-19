from django.db import models

class Weather(models.Model):
    region = models.CharField(max_length=30)
    Ttype = models.CharField(max_length=20)
    year = models.IntegerField()
    month = models.CharField(max_length=10)
    data = models.FloatField(null=True)
