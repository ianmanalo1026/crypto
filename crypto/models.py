
from django.db import models
from django.db.models.fields import DateTimeField


class CryptoData(models.Model):
    categories = models.CharField(max_length=50)
    time_and_date = DateTimeField(blank=True, null=True)
    prices = models.IntegerField(blank=True, null=True)
