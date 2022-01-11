from django.urls import path
from .views import *


urlpatterns = [
    path('', CompanyListView.as_view(), name='list'),
    path('<int:pk>', CompanyDetailView.as_view(), name='detail'),

    path(r'create/', CompanyCreateView.as_view(), name='create'),
    path(r'<int:pk>/update/', CompanyUpdateView.as_view(), name='update'),
    path(r'<int:pk>/delete/', CompanyDeleteView.as_view(), name='delete'),
]
