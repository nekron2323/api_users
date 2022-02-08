from django.urls import include, path
from rest_framework import routers

from .views import LoginView, LogoutView, PrivateUserViewSet, UserInfoViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register('users', UserInfoViewSet, basename='users')
router.register('private/users', PrivateUserViewSet, basename='admin')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
