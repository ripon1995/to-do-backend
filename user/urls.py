from django.urls import path
from user.views import UserCreateView

urlpatterns = [
    path('user/', UserCreateView.as_view()),
]
