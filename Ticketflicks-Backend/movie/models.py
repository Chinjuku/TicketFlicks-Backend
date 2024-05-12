from django.db import models
import uuid
from theatre.models import Theatre

# Create your models here.
class Actor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    actor_name = models.CharField(max_length=225)
    actor_img = models.ImageField(upload_to="uploads/actors", blank=True)

    def __str__(self):
        return self.actor_name

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category_name = models.CharField(max_length=225)
    
    def __str__(self):
        return self.category_name

class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    movie_name = models.CharField(max_length=255)
    movie_img = models.ImageField(upload_to="uploads/movies")
    movie_description = models.TextField(blank=True)
    price = models.FloatField()
    showing_date = models.DateField() # เริ่มฉายวันไหน
    show_time_mins = models.IntegerField() # แสดงหนังกี่นาที
    rating = models.FloatField()
    actors = models.ManyToManyField(Actor, blank=True)
    categories = models.ManyToManyField(Category)
    showing_due = models.DateField() # วันที่ฉายเสร็จสิ้น
    # favorite = models.ManyToManyField(IPAddress, related_name="ip_fav", blank=True)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE, related_name="movie_theatre")
    
    def __str__(self):
        return self.movie_name + " " + str(self.id)
    
class IPAddress(models.Model):
    ip = models.CharField(max_length=100)
    movieId = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="fav_ip")
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.ip + " " + str(self.favorite) + " " + str(self.movieId)