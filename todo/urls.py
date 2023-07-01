from django.urls import path
from .views import ToDoList, ToDoItem, ToDoTitleListView, ToDoCompletedTitleListView, SpecificToDoListView

urlpatterns = [
    path('todo/', ToDoList.as_view()),
    path('todo/<int:pk>/', ToDoItem.as_view()),
    path('todo/titles/', ToDoTitleListView.as_view()),
    path('todo/completed/', ToDoCompletedTitleListView.as_view()),
    path('todo/search/', SpecificToDoListView.as_view()),
]
