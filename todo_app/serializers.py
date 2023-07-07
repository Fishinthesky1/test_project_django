from rest_framework import serializers
from .models import Task, Comment, TimestampedModel
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class TaskViewSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    status = serializers.CharField(source='get_status_display')

    class Meta:
        model = Task
        fields = ('title', 'create_date', 'author', 'status')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class TaskDetailViewSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')
    author = UserSerializer
    users = UserSerializer(many=True, read_only=True)
    image = serializers.ImageField()
    due_date = serializers.DateTimeField(format="%Y-%m-%d")
    comments = CommentSerializer(many=True)

    class Meta:

        model = Task
        fields = ('status', 'author', 'users', 'image', 'due_date', 'comments')



