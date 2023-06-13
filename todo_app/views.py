from rest_framework import generics, permissions
from .models import Task, Comment
from .serializers import TaskViewSerializer, TaskDetailViewSerializer, CommentSerializer
from .service import PaginationTasks


class TaskView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskViewSerializer
    pagination_class = PaginationTasks

class TaskDetailView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailViewSerializer
    lookup_field = 'pk'


class CommentView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_comment = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        task_id = self.kwargs['task_id']
        return Comment.objects.filter(task_id=task_id)

    def perform_create(self, serializer):
        task_id = self.kwargs['task_id']
        task = Task.objects.get(id=task_id)
        serializer.save(task=task)