from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("core/", include(('core.urls', 'core'))),
]

if settings.DEBUG:
    urlpatterns += [
        path('api-auth', include('rest_framework.urls'))
    ]