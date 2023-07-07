from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('task/', views.TaskViewSet.as_view(actions={'get': 'list', 'post': 'create'})),
    path('task/<int:pk>/', views.TaskDetailViewSet.as_view(actions={'get': 'list', 'post': 'create'})),
    path('task/<int:task_id>/comments/', views.CommentViewSet.as_view(
        actions={'get': 'list', 'post': 'create'}), name='comments'
         ),
]
