from rest_framework import serializers
from .models import User, Idea, Comment
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'created_at', 'updated_at')

    def create(self, validated_data):
        user = User(email=validated_data['email'], username=validated_data['username'])
        password = validated_data['password']
        user.set_password(password)
        user.save()
        return user


class IdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idea
        fields = ('id', 'title', 'description', 'created_by', 'created_at', 'updated_at')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'idea', 'commenter', 'content', 'created_at', 'updated_at')
