from rest_framework. response import Response
from rest_framework.views import APIView

from .models import Task, Comment
from .serializers import TaskViewSerializer, TaskDetailViewSerializer, CommentSerializer


class TaskView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskViewSerializer(tasks, many=True)
        return Response(serializer.data)


class TaskDetailView(APIView):
    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        serializer = TaskDetailViewSerializer(task)
        return Response(serializer.data)


class CommentView(APIView):
    def get(self, request, task_id):
        comments = Comment.objects.filter(task_id=task_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, task_id):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(task_id=task_id)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)