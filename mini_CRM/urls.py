from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import RedirectView

from .views import IndexView


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('admin/', admin.site.urls),

    path(r'profile/', include(
        ('users.urls', 'profile')
    )),

    path(r'customer_info/', include(
        ('customer_info.urls', 'customer_info')
    )),

    path(r'do_projects/', include(
        ('do_projects.urls', 'do_projects')
    )),

    path(r'cooperation/', include(
        ('cooperation.urls', 'cooperation')
    )),

    path(r'profile/', include(
        ('users.urls', 'users')
    )),



    # path('', RedirectView.as_view(url='/customer_info/', permanent=True)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Add Django site authentication urls (for login, logout, password management)
# urlpatterns += [
#     path('accounts/', include('django.contrib.auth.urls')),
# ]

# Only add this when we in debug mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

