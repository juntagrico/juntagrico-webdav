"""
test URL Configuration for juntagrico_webdav development
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('impersonate/', include('impersonate.urls')),
    path('', include('juntagrico.urls')),
    path('', include('juntagrico_webdav.urls')),
]
