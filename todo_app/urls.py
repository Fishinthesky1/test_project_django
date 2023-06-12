from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('task/', views.TaskView.as_view()),
    path('task/<int:pk>/', views.TaskDetailView.as_view()),
    path('task/<int:task_id>/comments/', views.CommentView.as_view(), name='comments')
]
