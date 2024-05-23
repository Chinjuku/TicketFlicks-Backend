from django.db import models
from theatre.models import Place
# import uuid
# from backend.theatre.models import 

class Payment(models.Model):
    payment_id = models.CharField(unique=True, primary_key=True)
    client_secret = models.CharField()
    payment_method = models.CharField()
    seats = models.ManyToManyField(Place)
    amounts = models.FloatField()

