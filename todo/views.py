
from rest_framework.parsers import JSONParser
from rest_framework import generics, permissions
from utils.custom_response import custom_response
from todo.models import ToDo
from todo.serializers import ToDoSerializer
from rest_framework.response import Response


class ToDoList(generics.ListCreateAPIView):
    queryset = ToDo.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get('userId')
        if user_id:
            queryset = queryset.filter(user_id=user_id)

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ToDoSerializer(queryset, many=True)
        return Response(custom_response(serializer.data))

    def create(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        serializer = ToDoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(custom_response(serializer.data))

        return Response(custom_response(serializer.errors))


class ToDoItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    def retrieve(self, request, *args, **kwargs):
        data = self.get_object()
        serializer = self.get_serializer(data)
        print(serializer.data)
        return Response(custom_response(serializer.data))

    def update(self, request, *args, **kwargs):
        data = self.get_object()
        serializer = self.get_serializer(data, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        data.title = serializer.validated_data.get("title")
        serializer.save()
        return Response(serializer.data)


class ToDoTitleListView(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    def get_queryset(self):
        queryset = self.queryset.values_list('id', 'title')
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        titles = list(queryset)
        titles = [{'id': item[0], 'title': item[1]} for item in titles]
        return Response(custom_response(titles))


class ToDoCompletedTitleListView(generics.ListAPIView):
    queryset = ToDo.objects.all().filter(completed=True)
    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset.values_list('id', 'title', 'completed')
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        titles = list(queryset)
        titles = [{'id': item[0], 'title': item[1], 'completed': item[2]} for item in titles]
        return Response(custom_response(titles))


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
        return Response(custom_response(todos))
