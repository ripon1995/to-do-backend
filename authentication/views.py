from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from django.http import JsonResponse
from user.models import User
from utils.custom_response import custom_response
from rest_framework_simplejwt.tokens import RefreshToken


class LoginView(CreateAPIView):

    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = User.objects.filter(email=username, password=password).first()

        if user is None:
            return JsonResponse(custom_response(user))

        refresh_token = RefreshToken.for_user(user)
        access_token = refresh_token.access_token

        data = {
            "access_token": str(access_token),
            "refresh_token": str(refresh_token)
        }
        return Response(custom_response(data))
