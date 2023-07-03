from django.urls import path
from .views import ToDoListCreateView, ToDoRetrieveUpdateDestroyView, ToDoTitleListView, ToDoCompletedTitleListView, SpecificToDoListView

urlpatterns = [
    path('todo/', ToDoListCreateView.as_view()),
    path('todo/<int:pk>/', ToDoRetrieveUpdateDestroyView.as_view()),
    path('todo/titles/', ToDoTitleListView.as_view()),
    path('todo/completed/<str:completed>/', ToDoCompletedTitleListView.as_view()),
    path('todo/search/', SpecificToDoListView.as_view()),
]
