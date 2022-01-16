from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *


urlpatterns = [
    path('managers/', UserListView.as_view(), name='list'),
    path('register/', RegisterCreateView.as_view(), name='register'),
    path('profile/', profile, name='profile'),
    # path('profile/', ProfileFormView.as_view(), name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
