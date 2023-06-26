from rest_framework import serializers
from .models import User, Idea, Comment, Tag, IdeaRating, Notification, Progress

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


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'ideas')

class IdeaSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        queryset=Tag.objects.all(),
        slug_field='name',
        many=True,
        required=False
    )

    class Meta:
        model = Idea
        fields = ('id', 'title', 'description', 'tags', 'created_by', 'created_at', 'updated_at')

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        idea = Idea.objects.create(**validated_data)

        for tag_name in tags_data:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            idea.tags.add(tag)

        return idea

    def update(self, instance, validated_data):
        # Check if instance exists, otherwise create a new instance
        if instance is None:
            return self.create(validated_data)

        # Update the idea fields
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)

        # Update the idea tags
        tags_data = validated_data.get('tags')
        if tags_data is not None:
            instance.tags.clear()  # Clear existing tags

            for tag_name in tags_data:
                tag, _ = Tag.objects.get_or_create(name=tag_name)
                instance.tags.add(tag)

        instance.save()
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        tags = representation.pop('tags')
        if tags is not None:
            if not isinstance(tags, list):
                tags = [tags]
            representation['tags'] = [tag for tag in tags]
        return representation


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'idea', 'commenter', 'content', 'created_at', 'updated_at')

class IdeaRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdeaRating
        fields = ('id', 'idea', 'rater', 'value')

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id', 'idea', 'user', 'message', 'is_read', 'created_at')


class ProgressSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.username') # might use email instead

    class Meta:
        model = Progress
        fields = '__all__'