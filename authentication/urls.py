from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from .views import LoginView

urlpatterns = [
    path('token/', LoginView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view())
]
