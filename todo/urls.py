from django.urls import path
from .views import ToDoListCreateView, ToDoRetrieveUpdateDestroyView, ToDoTitleListView, ToDoCompletedTitleListView, \
    ToDoListSearchFilterApi, ToDoFilterView

urlpatterns = [
    path('todo/', ToDoListCreateView.as_view()),
    path('todo/<int:pk>/', ToDoRetrieveUpdateDestroyView.as_view()),
    path('todo/titles/', ToDoTitleListView.as_view()),
    path('todo/completed/<str:completed>/', ToDoCompletedTitleListView.as_view()),
    path('todo/search/', ToDoListSearchFilterApi.as_view()),
    path('todo/filtered/', ToDoFilterView.as_view())
]
