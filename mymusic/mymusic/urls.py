"""
URL configuration for mymusic project.

"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('music.urls')),
    
    path('admin/', admin.site.urls),
]
