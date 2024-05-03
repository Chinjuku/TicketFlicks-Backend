from django.db import models
import uuid
from theatre.models import Theatre

# Create your models here.
class Actor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    actor_name = models.CharField(max_length=225)

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
    movie_description = models.TextField()
    price = models.FloatField()
    showing_date = models.DateField() # เริ่มฉายวันไหน
    # Showtime รอบฉาย
    start_time = models.DateTimeField() # เริ่มฉายเวลา
    end_time = models.DateTimeField() # ฉายเสร็จสิ้นเวลา
    rating = models.FloatField() 
    actors = models.ManyToManyField(Actor)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categories")
    showing_due = models.DateField() # วันที่ฉายเสร็จสิ้น
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE, related_name="movie_theatre")

    def __str__(self):
        return self.movie_name