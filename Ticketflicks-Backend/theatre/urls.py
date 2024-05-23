from django.urls import path
from theatre import api
# from .views import CreateTheatre

urlpatterns = [
    path('createtheatre/', api.create_theatre),
    path('alltheatre/<uuid:movieId>/<str:date>/', api.all_theatre), # Show all theatres that showing from Movie
    path('theatre/<uuid:pk>/', api.theatre), # Show selected theatre from Movie
    path('place/<uuid:pk>/', api.place),
    path('place/select_seat/', api.select_place),
    path('place/update_seat/', api.update_seat)
]