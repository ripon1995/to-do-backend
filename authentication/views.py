from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from user.models import User
from utils.custom_response import custom_response
from rest_framework_simplejwt.tokens import RefreshToken


class LoginView(CreateAPIView):

    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(email=username).first()

        if user is None:
            return Response(custom_response(user))

        refresh_token = RefreshToken.for_user(user)

        data = {
            "access_token": str(refresh_token.access_token),
            "refresh_token": str(refresh_token)
        }
        return Response(custom_response(data))
