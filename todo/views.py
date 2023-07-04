from django.db.models import F
from .pagination import ToDoListPaginationClass
from rest_framework import generics, permissions, status
from todo.models import ToDo
from todo.serializers import ToDoSerializer, ToDoTitleSerializer
from todo.filters import CustomSearchFilter
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


# if the user is logged in then to do can be created
# also todo list can be fetched with query param
class ToDoListCreateView(generics.ListCreateAPIView):
    pagination_class = ToDoListPaginationClass
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user_id']
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.order_by(F('createdDate').asc())

    def create(self, request, *args, **kwargs):
        user = self.request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


# We will get todo list for logged in user
class ToDoListViewForLoggedInUser(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = ToDoListPaginationClass
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        queryset = self.queryset.filter(user_id=user_id)
        queryset = queryset.order_by(F('createdDate').asc())
        return queryset


class ToDoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    def retrieve(self, request, *args, **kwargs):
        data = self.get_object()
        serializer = self.get_serializer(data)
        print(serializer.data)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        data = self.get_object()
        serializer = self.get_serializer(data, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=204, data={"message": "success"})


class ToDoTitleListView(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoTitleSerializer


class ToDoCompletedTitleListView(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoTitleSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'completed'

    def get_queryset(self):
        user_id = self.request.user.id
        completed = self.kwargs.get('completed', True)
        queryset = self.queryset.filter(completed=completed, user_id=user_id)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ToDoListSearchFilterApi(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoTitleSerializer
    filter_backends = [CustomSearchFilter]
    search_fields = ['title', 'description', 'id']


class ToDoFilterView(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'description']
