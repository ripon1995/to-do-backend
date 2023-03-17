from django.urls import path
from .views import ToDoList, ToDoItem, ToDoTitleListView

urlpatterns = [
    path('todo/', ToDoList.as_view()),
    path('todo/<int:pk>/', ToDoItem.as_view()),
    path('todo/titles/', ToDoTitleListView.as_view())
]
