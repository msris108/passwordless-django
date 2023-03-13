from rest_framework.response import Response
from rest_framework.decorators import api_view

# Authenticated with Django TokenAuthentication

@api_view(['GET'])
def index(request):
    return Response({"message": "Hello, " + str(request.user)})
