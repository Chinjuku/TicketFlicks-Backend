from django.urls import path

from movie.api import movie, ipaddress, category

urlpatterns = [
    path('movie/', movie.all_movie),
    path('movie/<uuid:pk>/', movie.select_movie),
    path('movie/recommand/', movie.recommand_movie),
    path('movie/onshow/', movie.onshow_movie),
    path('movie/comming/', movie.comming_movie),
    path('movie/fav/', movie.favorite_movie),
    path('ip/fav/<uuid:movieId>/', ipaddress.all_fav),
    path('category/', category.all_categories),
]