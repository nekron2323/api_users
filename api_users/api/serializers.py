from rest_framework import serializers

from users.models import City, User


class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'other_name',
                  'email', 'phone', 'birthday', 'is_admin')


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')


class UpdateUserResponseModel(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'other_name',
                  'email', 'phone', 'birthday')
