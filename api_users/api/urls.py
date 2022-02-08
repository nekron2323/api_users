from django.urls import include, path
from rest_framework import routers

from .views import LoginView, LogoutView, UserInfoViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register('users', UserInfoViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
