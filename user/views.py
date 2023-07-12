from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework.response import Response

from notifications.push_notifications import send_push_notification
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


class UserRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        data = self.get_object()
        serializer = self.get_serializer(data)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class UserPasswordUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        user.password = serializer.validated_data.get("password")
        serializer.save()
        return Response(serializer.data)


class Me(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class SendPushNotificationToUser(generics.RetrieveAPIView):
    queryset = User.objects.all()

    def get_object(self):
        user_id = self.kwargs.get('user_id')
        user = get_object_or_404(self.queryset, id=user_id)
        return user

    def retrieve(self, request, *args, **kwargs):
        user = self.get_object()
        device_token = user.device_token
        title = request.data.get('title')
        body = request.data.get('body')

        send_push_notification(device_token, title, body)

        return Response("Push Notification send to the user")
