from rest_framework import serializers
from .models import User, Idea, Comment
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'created_at', 'updated_at')

class IdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idea
        fields = ('id', 'title', 'description', 'created_by', 'created_at', 'updated_at')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'idea', 'commenter', 'content', 'created_at', 'updated_at')
