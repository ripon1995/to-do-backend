from rest_framework import generics
from rest_framework.response import Response
from user.models import User
from user.serializers import UserSerializer
from rest_framework.parsers import JSONParser


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()

    # serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


class UserRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        data = self.get_object()
        serializer = self.get_serializer(data)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        user.username = request.data.get("username")
        user.save()
        serializer = self.get_serializer(user)
        return Response(serializer.data)
