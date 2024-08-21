from rest_framework import serializers
from .models import OficialUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = OficialUser
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

    def create(self, validated_data):
        user = OficialUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user
