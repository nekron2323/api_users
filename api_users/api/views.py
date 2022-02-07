from rest_framework import viewsets

from .serializers import CurrentUserResponseModelSerializer
from users.models import User


class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CurrentUserResponseModelSerializer
    http_method_names = ('get', )
