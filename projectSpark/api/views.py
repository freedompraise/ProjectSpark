# rest framework
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import generics
# root
from .serializers import UserSerializer
from .models import User
# django
from django.contrib.auth import authenticate
# jwt
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication


class UserRegistrationView(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token_serializer = TokenObtainPairSerializer()
            token = token_serializer.get_token(user)
            return Response({'access': str(token.access_token), 'refresh': str(token)})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserAuthenticationView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    serializer_class = TokenObtainPairSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.user
        token = serializer.validated_data['access']
        return Response({'token': token})