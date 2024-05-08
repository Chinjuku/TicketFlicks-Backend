from django.urls import path
from theatre import api
# from .views import CreateTheatre

urlpatterns = [
    path('createtheatre/', api.create_theatre),
    path('theatre/<uuid:pk>/', api.theatre),
    path('place/<uuid:pk>', api.place),
    path('place/select_seat/', api.select_place)
]