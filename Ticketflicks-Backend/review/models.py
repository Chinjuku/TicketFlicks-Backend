from django.db import models
import uuid
from django.core.validators import MaxValueValidator
from movie.models import Movie

class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default="unknown")
    review_comment = models.TextField()
    stars = models.IntegerField(validators=[MaxValueValidator(5)])
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="review_movie")
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name) + " " + str(self.review_comment) + " " + str(self.id) + " " + str(self.time_stamp)

class Reply(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    review_id = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="reply_review")
    name = models.CharField(max_length=255, default="unknown")
    reply_comment = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name) + " " + str(self.reply_comment) + " " + str(self.review_id.id)