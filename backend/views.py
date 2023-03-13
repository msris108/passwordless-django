from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict
from .serializers import UserSerializer
from .models import CustomUser

# Authenticated with Django TokenAuthentication

@api_view(['GET'])
def index(request):
    '''Health check, basic auth token'''
    return Response({"message": "Hello, " + str(request.user)})

@api_view(['GET'])
def getCurrentUser(request):
    '''Get current user info'''
    serializer = UserSerializer(model_to_dict(request.user))
    if serializer.is_valid: 
        return Response(serializer.data)
    return Response(serializer.error_messages)

@api_view(['GET'])
def getUserByEmail(request, email): 
    '''Get user by email : only for superusers'''
    if request.user.is_superuser:
        serializer = UserSerializer(CustomUser.objects.filter(email=email).values()[0])
        if serializer.is_valid:
            return Response(serializer.data)
        return Response(serializer.error_messages)
    return Response({"message": "access denied"})

@api_view(['GET'])
def getAllUsers(request):
    '''Get all user : only for superusers'''
    if request.user.is_superuser:
        serializer = UserSerializer(CustomUser.objects.all().values(), many=True)
        if serializer.is_valid:
            return Response(serializer.data)
        return Response(serializer.error_messages)
    return Response({"message": "access denied"})
