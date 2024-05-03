from django.db import models
import uuid

# Create your models here.
class Theatre(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    theatre_num = models.IntegerField()

    def __str__(self):
        return str(self.theatre_num)

class Place(models.Model): # ที่นั่ง
    class TypeInSeat(models.TextChoices):
        NORMAL = 'normal'
        VIP = 'vip'
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    seat_num = models.CharField(max_length=225) # A1 - F100
    type = models.CharField(
        choices=TypeInSeat.choices,
        default=TypeInSeat.NORMAL,
    )
    isIdle = models.BooleanField(default=True)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE, related_name="place_theatre")

    def __str__(self):
        return self.seat_num
