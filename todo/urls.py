from django.urls import path
from .views import ToDoList

urlpatterns = [
    path('todo/', ToDoList.as_view())
]
