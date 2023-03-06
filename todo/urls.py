from django.urls import path
from todo import views

urlpatterns = [
    path('todo/', views.to_do_list)
]
