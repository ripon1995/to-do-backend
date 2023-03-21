from rest_framework import generics

from todo.custom_response import custom_response
from user.models import User
from user.serializers import UserSerializer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()

    # serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(custom_response(serializer.data))

        return JsonResponse(custom_response(serializer.errors))
