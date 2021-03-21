# djangoChannels/urls.py
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('chat/', include('chat.urls')),
    path('users/', include('user_.urls')),
    path('admin/', admin.site.urls),
]
