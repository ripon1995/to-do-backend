from rest_framework.parsers import JSONParser
from rest_framework import generics
from todo.custom_response import custom_response
from todo.models import ToDo
from todo.serializers import ToDoSerializer
from django.http import JsonResponse


class ToDoList(generics.ListCreateAPIView):
    queryset = ToDo.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ToDoSerializer(queryset, many=True)
        return JsonResponse(custom_response(serializer.data))

    def create(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        serializer = ToDoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(custom_response(serializer.data))

        return JsonResponse(custom_response(serializer.errors))


class ToDoItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    def retrieve(self, request, *args, **kwargs):
        data = self.get_object()
        serializer = self.get_serializer(data)
        print(serializer.data)
        return JsonResponse(custom_response(serializer.data))

    def update(self, request, *args, **kwargs):
        data = self.get_object()
        serializer = self.get_serializer(data, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(custom_response(serializer.data))


class ToDoTitleListView(generics.ListAPIView):
    serializer_class = ToDoSerializer

    def get_queryset(self):
        todos = ToDo.objects.all()
        queryset = todos.values_list('id', 'title')
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        titles = list(queryset)
        titles = [{'id': item[0], 'title': item[1]} for item in titles]
        return JsonResponse(custom_response(titles))


class ToDoCompletedTitleListView(generics.ListAPIView):
    serializer_class = ToDoSerializer

    def get_queryset(self):
        completed_queryset = ToDo.objects.all().filter(completed=True)
        queryset = completed_queryset.values_list('id', 'title', 'completed')
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        titles = list(queryset)
        titles = [{'id': item[0], 'title': item[1], 'completed': item[2]} for item in titles]
        return JsonResponse(custom_response(titles))


class SpecificToDoListView(generics.ListAPIView):
    def get_queryset(self):
        specific_word = self.kwargs['specific_word']
        todos_queryset = ToDo.objects.all().filter(title__icontains=specific_word)
        queryset = todos_queryset.values_list('id', 'title', 'description')
        print(queryset)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        todos = list(queryset)
        todos = [{'id': item[0], 'title': item[1], 'description': item[2]} for item in todos]
        return JsonResponse(custom_response(todos))
