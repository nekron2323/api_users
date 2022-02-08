from django.conf import settings
from urllib import request
from rest_framework import mixins, status, viewsets
from rest_framework.authentication import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import CurrentUserSerializer

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'access': refresh.access_token
    }

class LoginView(APIView):
    def post(self, request, format=None):
        data = request.data
        response = Response()
        message = 'Неверно переданы поля:'
        flag = True
        try:
            login = data['login']
        except KeyError:
            flag = False
            message += ' login'
        try:
            password = data['password']
        except KeyError:
            flag = False
            message += ' password'
        if not flag:
            return Response(
                {
                    'code': status.HTTP_400_BAD_REQUEST,
                    'message': message
                }
            )
        user = authenticate(username=login, password=password)
        if user is not None:
            if user.is_active:
                data = get_tokens_for_user(user)
                response.set_cookie(
                    key=settings.SIMPLE_JWT['AUTH_COOKIE'],
                    value=data["access"],
                    expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                    secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                    httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                    samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
                )
                response.data = CurrentUserSerializer(user).data
                return response
        return Response(
            {"Ошибка": "Неправильный логин или пароль"},
            status=status.HTTP_404_NOT_FOUND
        )

class LogoutView(APIView):
    def get(self, request):
        response = Response()
        response.delete_cookie(key=settings.SIMPLE_JWT['AUTH_COOKIE'])
        response.data = "Вы вышли из системы"
        return response