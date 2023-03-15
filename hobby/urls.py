from django.urls import path
from hobby import views

urlpatterns = [
    path('hobby/', views.hobby_views)
]
