from rest_framework import serializers

from users.models import User, City


class CitiesModelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = City


class CurrentUserResponseModelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('first_name', 'last_name', 'other_name',
                  'email', 'phone', 'birthday')
        model = User
