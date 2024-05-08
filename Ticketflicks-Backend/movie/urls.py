from django.urls import path

from movie.api import movie

urlpatterns = [
    path('movie/', movie.all_movie),
    path('movie/<uuid:pk>/', movie.select_movie),
    path('movie/recommand/', movie.recommand_movie),
    path('movie/onshow/', movie.onshow_movie),
    path('movie/comming/', movie.comming_movie),
    path('movie/fav/', movie.favorite_movie)
]