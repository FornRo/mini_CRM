from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *


urlpatterns = [
    path('', ProjectListView.as_view(), name='list'),
    path('<int:pk>', ProjectDetailView.as_view(), name='detail'),
    path(r'create/', ProjectCreateView.as_view(), name='create'),
    path(r'<int:pk>/update/', ProjectUpdateView.as_view(), name='update'),
    path(r'<int:pk>/delete/', ProjectDeleteView.as_view(), name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
