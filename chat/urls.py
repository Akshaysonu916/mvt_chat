from django.urls import path
from django.contrib.auth import views as auth_views
from . import views 
urlpatterns = [
    path('', views.home_view, name='home'),
    path('chat/<str:room_name>/', views.chat_room, name='chat'),
    path('users/', views.user_list_view, name='user_list'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
]