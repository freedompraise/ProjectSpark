# rest framework
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import generics
# root
from .serializers import (
    UserSerializer,
    IdeaSerializer,
    CommentSerializer,
)
from .models import (
    User,
    Idea,
    Comment,
)
# django
from django.contrib.auth import authenticate
# jwt
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

#REGISTRATION   
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

#AUTHENTICATION
class UserAuthenticationView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = response.data.get('access')
        if token:
            return Response({'token': token}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# CREATE AND LIST IDEAS
class IdeaListAPIView(generics.ListCreateAPIView):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer
    permission_classes = (AllowAny,)
    authentication_classes = [JWTAuthentication]

# RETRIEVE, UPDATE AND DELETE IDEAS
class IdeaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer
    permission_classes = (AllowAny,)
    authentication_classes = [JWTAuthentication]

# CREATE COMMENTS
class CommentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = (AllowAny,)
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        idea_id = self.kwargs['idea_id']
        serializer.save(idea_id=idea_id)
    
    def get_queryset(self):
        idea_id = self.kwargs['idea_id']
        return Comment.objects.filter(idea_id=idea_id)

# LIST COMMENTS
class CommentListAPIView(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = (AllowAny,)
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        idea_id = self.kwargs['idea_id']
        return Comment.objects.filter(idea_id=idea_id)


# RETRIEVE, UPDATE AND DELETE COMMENTS
class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (AllowAny,)
    authentication_classes = [JWTAuthentication]
