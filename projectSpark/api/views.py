# rest framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import(
    filters,
    generics,
    status,
    viewsets,
) 
# root
from .serializers import (
    UserSerializer,
    IdeaSerializer,
    CommentSerializer,
    TagSerializer,
)
from .models import (
    User,
    Idea,
    Comment,
    Tag,
)
# django
from django.contrib.auth import authenticate
from django.http import request
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.utils.text import slugify
# jwt
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer 
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

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
            return Response({'access': str(token.access_token), 'refresh': str(token), 'user': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# UserAuthenticationView
# class UserAuthenticationView(TokenObtainPairView):
#     serializer_class = TokenObtainPairSerializer

#     def post(self, request, *args, **kwargs):
#         response = super().post(request, *args, **kwargs)
#         if response.status_code == status.HTTP_200_OK:
#             token = response.data.get('access')
#             return Response({'token': token}, status=status.HTTP_200_OK)
#         return Response({'error': 'Invalid credentials'}, status=response.status_code)


# UserLoginView
class UserLoginView(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = User.objects.filter(email=email).first()

        if user and user.check_password(password):
            return Response(
                {
                    'message': 'Login successful',
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {'detail': 'Invalid credentials'},
                status=status.HTTP_401_UNAUTHORIZED
            )


# CREATE AND LIST IDEAS
class IdeaListAPIView(generics.ListCreateAPIView):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer
    permission_classes = (AllowAny,)
    authentication_classes = [JWTAuthentication]
    # TO DO
    # def get_queryset(self):
    #     user_id = request.user.id
    #     return Idea.objects.filter(created_by=user_id)
    

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

# TAGS 
class TagListAPIView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (AllowAny,)
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        tag_name = self.request.data.get('name')  # Assuming the tag name is provided in the request data
        slug = Tag.generate_unique_slug(tag_name)
        serializer.save(slug=slug)