from rest_framework import serializers

from users.models import User


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


class PrivateUserModel(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'city')


class PrivateDetailUserModel(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'other_name', 'email', 'phone',
                  'birthday', 'city', 'additional_info', 'is_admin', 'username', 'password')
