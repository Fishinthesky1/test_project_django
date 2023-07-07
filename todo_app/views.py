from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Task, Comment
from .serializers import TaskViewSerializer, TaskDetailViewSerializer, CommentSerializer
from .pagination import PaginationTasks


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskViewSerializer
    pagination_class = PaginationTasks


class TaskDetailViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskDetailViewSerializer
    lookup_field = 'pk'


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_comment = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        task_id = self.kwargs['task_id']
        return Comment.objects.filter(task_id=task_id)

    def perform_create(self, serializer):
        task_id = self.kwargs['task_id']
        task = Task.objects.get(id=task_id)
        serializer.save(task=task)