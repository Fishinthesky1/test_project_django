from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'tasks'

urlpatterns = [
    path('', views.Tasks, name='task_list'),
    path('new-task/', views.newTask, name='new-task')
]
