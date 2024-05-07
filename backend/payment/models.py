from django.db import models
import uuid
from backend.theatre.models import Place, Theatre

# Create your models here.
# To check about select tickets
# class Ticket(models.Model):
#     theatreId = models.ForeignKey(Theatre)
#     placeId = models.ForeignKey(Place)
#     amount = models.FloatField()


# class Payment(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
#     ticket = models.ManyToManyField(Ticket)
#     amount = models.FloatField()    
