from rest_framework import serializers
from .models import User, Idea, Comment, Tag
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

class TagField(serializers.StringRelatedField):
    def to_internal_value(self, data):
        # Return the tag name as-is
        return data

    def to_representation(self, value):
        if isinstance(value, Tag):
            # Convert Tag instance to its name for serialization
            return value.name
        return super().to_representation(value)


class IdeaSerializer(serializers.ModelSerializer):
    tags = TagField(many=True, required=False)

    class Meta:
        model = Idea
        fields = ('id', 'title', 'description','tags', 'created_by', 'created_at', 'updated_at')

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        idea = Idea.objects.create(**validated_data)

        for tag_data in tags_data:
            tag, _ = Tag.objects.get_or_create(name=tag_data)
            idea.tags.add(tag_id)

        if not tags_data:
            idea.tags.clear()

        return idea

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', [])
        instance = super().update(instance, validated_data)

        instance.tags.clear()
        for tag_name in tags_data:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            instance.tags.add(tag)

        return instance
        

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'idea', 'commenter', 'content', 'created_at', 'updated_at')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'ideas')