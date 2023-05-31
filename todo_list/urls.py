from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('oauth.urls', namespace='oauth')),
    path('todo_app/', include('todo_app.urls', namespace='todo_app')),
]

