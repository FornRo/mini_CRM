from django.urls import path, include
from . import views


urlpatterns = [
    path('', include([
        path('', views.CompanyListView.as_view(), name='list'),
        path('<int:pk>', views.CompanyDetailView.as_view(), name='detail'),

        path(r'create/', views.CompanyCreateView.as_view(), name='create'),
        path(r'<int:pk>/update/', views.CompanyUpdateView.as_view(), name='update'),
        path(r'<int:pk>/delete/', views.CompanyDeleteView.as_view(), name='delete'),
    ])
         ),

]
