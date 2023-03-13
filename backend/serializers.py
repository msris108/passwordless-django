from rest_framework import serializers

from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    ''' Serializes the custom user class '''
    class Meta:
        model = CustomUser
        exclude = 'password',