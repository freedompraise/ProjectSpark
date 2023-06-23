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
    IdeaRatingSerializer,
)
from .models import (
    User,
    Idea,
    Comment,
    Tag,
    IdeaRating,
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
# yasg
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

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

    def put(self, request, *args, **kwargs):
        idea = self.get_object()
        serializer = self.get_serializer(idea, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        idea = self.get_object()
        serializer = self.get_serializer(idea, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

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

class IdeaListByTagAPIView(generics.ListAPIView):
    serializer_class = IdeaSerializer
    permission_classes = (AllowAny,)
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        tag_slug = self.kwargs['tag_slug']
        tag = Tag.objects.get(slug=tag_slug)
        return Idea.objects.filter(tags=tag)

class IdeaRatingCreateAPIView(generics.CreateAPIView):
    queryset = IdeaRating.objects.all()
    serializer_class = IdeaRatingSerializer
    permission_classes = (AllowAny,)
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        idea_id = self.kwargs['idea_id']
        idea = Idea.objects.get(pk=idea_id)
        if self.request.user.is_authenticated:
            serializer.save(rater=self.request.user, idea=idea)
            idea.update_total_rating()
        else:
            return Response({'error': 'Authentication is required to rate an idea.'}, status=status.HTTP_401_UNAUTHORIZED)
            
    def perform_update(self, serializer):
        serializer.save()
        self.get_object().update_total_rating()
       

class IdeaRatingListAPIView(generics.ListAPIView):
    serializer_class = IdeaRatingSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        idea_id = self.kwargs['idea_id']
        return IdeaRating.objects.filter(idea_id=idea_id)