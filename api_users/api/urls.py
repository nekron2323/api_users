from django.urls import include, path
from rest_framework import routers

from .views import LoginView, LogoutView

app_name = 'api'

router = routers.DefaultRouter()


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
