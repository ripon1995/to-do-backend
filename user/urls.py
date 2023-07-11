from django.urls import path
from user.views import UserCreateView, UserRetrieveUpdateDeleteView, UserPasswordUpdateView, Me, \
    SendPushNotificationToUser

urlpatterns = [
    path('user/', UserCreateView.as_view()),
    path('user/<int:pk>/', UserRetrieveUpdateDeleteView.as_view()),
    path('user/<int:pk>/password/', UserPasswordUpdateView.as_view()),
    path('user/me/', Me.as_view()),
    path('notification/<int:user_id>/', SendPushNotificationToUser.as_view())
]
