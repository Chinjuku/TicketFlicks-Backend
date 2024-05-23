# myproject/urls.py

from django.urls import path
from .api import payment, get_payment

urlpatterns = [
    path('payment/', payment),
    path('payment/<str:pk>/', get_payment),
]
