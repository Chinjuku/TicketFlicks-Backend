from django.urls import path

from movie import api

urlpatterns = [
    path('movie/', api.movie_data),
]