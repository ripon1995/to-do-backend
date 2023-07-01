from rest_framework.parsers import JSONParser
from rest_framework import generics, permissions
from todo.models import ToDo
from todo.serializers import ToDoSerializer, ToDoTitleSerializer
from rest_framework.response import Response


class ToDoList(generics.ListCreateAPIView):
    queryset = ToDo.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = self.filter_queryset(queryset)
        return queryset

    def filter_queryset(self, queryset):
        user_id = self.request.query_params.get('userId')
        if user_id:
            queryset = queryset.filter(user__id=user_id)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ToDoSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        serializer = ToDoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


class ToDoItem(generics.RetrieveUpdateDestroyAPIView):
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

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ToDoCompletedTitleListView(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoTitleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset.filter(completed=True)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class SpecificToDoListView(generics.ListAPIView):
    queryset = ToDo.objects.all()

    def get_queryset(self):
        specific_word = self.kwargs['specific_word']
        queryset = self.queryset.filter(title__icontains=specific_word)
        queryset = queryset.values_list('id', 'title', 'description')
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        todos = list(queryset)
        todos = [{'id': item[0], 'title': item[1], 'description': item[2]} for item in todos]
        return Response(todos)
