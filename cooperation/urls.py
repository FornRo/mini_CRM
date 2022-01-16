from django.urls import path
from .views import *


urlpatterns = [
    path('', CooperationListView.as_view(), name='list'),
    path('company/<int:pk>', CooperationByCompanyListView.as_view(), name='list_company'),
    path('project/<int:pk>', CooperationByProjectListView.as_view(), name='list_project'),
    path('user/<int:pk>', CooperationByUserListView.as_view(), name='list_user'),
    path('<int:pk>', CooperationDetailView.as_view(), name='detail'),

    path(r'create/', CooperationCreateView.as_view(), name='create'),
    path(r'<int:pk>/update/', CooperationUpdateView.as_view(), name='update'),
    path(r'<int:pk>/delete/', CooperationDeleteView.as_view(), name='delete'),
]
