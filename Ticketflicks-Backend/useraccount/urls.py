from django.urls import path

from dj_rest_auth.jwt_auth import get_refresh_view
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView
from rest_framework_simplejwt import views as jwt_views
from .views import CustomTokenObtainPairView

from . import api

urlpatterns = [
    path('register/', api.createUser, name='rest_register'),
    path('login/', LoginView.as_view(), name='rest_login'),
    path('logout/', LogoutView.as_view(), name='rest_logout'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('token/', 
         CustomTokenObtainPairView.as_view(), 
         name ='token_obtain_pair'), 
    path('<uuid:pk>/', api.getUser, name='api_getUser'),
    path('edit/<uuid:pk>/', api.editUser, name='api_editUser'),
]