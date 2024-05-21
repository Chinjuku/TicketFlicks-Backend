from django.db.models.signals import post_save
from datetime import datetime, timedelta
from django.dispatch import receiver
from django.db import models
from movie.models import Movie
import uuid

# Create your models here.
class Theatre(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    theatre_num = models.IntegerField()
    show_time = models.DateTimeField(blank=True)
    is_show = models.BooleanField(default=True) # ถ้า True = เปิดจองได้ แต่ ถ้า False = ปิดจองหรือฉายหนังเสร็จสิ้นละ (show_time+2hr)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="movie_shows")

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
        return str(self.id) + " " + self.seat_num + " , Theatre : " + str(self.theatre.theatre_num) + ", Datetime : " + self.theatre.show_time.strftime('%Y-%m-%d %H:%M')

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

# @receiver(post_save, sender=Theatre)
# def update_theatres(sender, instance, created, **kwargs):
#     # Check if the instance is being created or updated
#     if created or instance.is_show:
#         # Perform your logic to update the instance here
#         now = datetime.today() - timedelta(hours=2)
#         instance.is_show = False if instance.show_time <= now else True
#         instance.save()
