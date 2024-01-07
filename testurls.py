"""
test URL Configuration for juntagrico_webdav development
"""
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('juntagrico.urls')),
    path('', include('juntagrico_webdav.urls')),
]
