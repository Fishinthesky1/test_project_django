from django.urls import path
from . import views

app_name = 'oauth'

urlpatterns =[
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('new-user/', views.register, name='new-user'),
    path('users/', views.usersView, name='users'),
    path('users/profile', views.profile, name='profile'),
    path('users/<int:profile_id>/', views.user_view, name='user'),
]