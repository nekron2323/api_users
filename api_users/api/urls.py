from django.urls import include, path
from rest_framework import routers

from .views import UserInfoViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register('user', UserInfoViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls))
]
