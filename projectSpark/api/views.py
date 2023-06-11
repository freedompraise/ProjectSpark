# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from .models import User

class UserRegistrationView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserAuthenticationView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = User.objects.filter(username=username).first()
        if user is None or not user.check_password(password):
            return Response({"message": "Invalid username or password."}, status=status.HTTP_400_BAD_REQUEST)
        # You can implement your own token generation or use a library like Django REST framework JWT for authentication
        # Example: generate token
        # token = generate_token(user)
        return Response({"message": "User authenticated successfully.", "token": token}, status=status.HTTP_200_OK)
