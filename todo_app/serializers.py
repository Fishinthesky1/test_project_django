from rest_framework import serializers
from .models import Task, Comment

class TaskViewSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
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
    author = serializers.StringRelatedField()
    users = serializers.SlugRelatedField(slug_field='username', many=True, read_only=True)
    image = serializers.ImageField()
    create_date = serializers.DateTimeField(format="%Y-%m-%d")
    update_time = serializers.DateTimeField(format="%Y-%m-%d")
    due_date = serializers.DateTimeField(format="%Y-%m-%d")
    comments = CommentSerializer(many=True)

    class Meta:

        model = Task
        fields = "__all__"


