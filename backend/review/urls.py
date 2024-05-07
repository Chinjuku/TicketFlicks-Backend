from django.urls import path
from review import api

urlpatterns = [
    path('review/<uuid:movieId>/', api.review),
    path('reply/<uuid:reviewId>/', api.reply),
]