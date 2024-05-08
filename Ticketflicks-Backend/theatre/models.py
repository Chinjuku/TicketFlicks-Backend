from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

import uuid

# Create your models here.
class Theatre(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    theatre_num = models.IntegerField()
    show_time = models.DateTimeField(blank=True)

    def __str__(self):
        return str(self.theatre_num) + " Datetime : " + self.show_time.strftime('%Y-%m-%d %H:%M') + " " + str(self.id)

class Place(models.Model): # ที่นั่ง
    class TypeInSeat(models.TextChoices):
        NORMAL = 'normal'
        VIP = 'vip'
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    seat_num = models.CharField(max_length=225) # A1 - F12
    type = models.CharField(
        choices=TypeInSeat.choices,
        default=TypeInSeat.NORMAL,
    )
    isIdle = models.BooleanField(default=True)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE, related_name="place_theatre")

    def __str__(self):
        return self.seat_num + " , Theatre : " + str(self.theatre.theatre_num) + ", Datetime : " + self.theatre.show_time.strftime('%Y-%m-%d %H:%M')

@receiver(post_save, sender=Theatre)
def create_places(sender, instance, created, **kwargs):
    if created:
        # Create places for the theatre
        for row in ['A', 'B', 'C', 'D', 'E']:
            for i in range(1, 12):
                seat_num = f"{row}{i}"
                type = 'normal'
                if (row == 'E'):
                    type = 'vip'
                Place.objects.create(seat_num=seat_num, theatre=instance, type=type)
