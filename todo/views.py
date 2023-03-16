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
