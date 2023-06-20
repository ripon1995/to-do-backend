from django.urls import path
from user.views import UserCreateView, UserRetrieveView, UserPasswordUpdateView

urlpatterns = [
    path('user/', UserCreateView.as_view()),
    path('user/<int:pk>/', UserRetrieveView.as_view()),
    path('user/<int:pk>/password/', UserPasswordUpdateView.as_view()),
]
