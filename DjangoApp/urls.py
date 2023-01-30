from django.contrib import admin
from django.urls import path, include
from other import views
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('other/', include('other.urls')),
    path('shorten/', include('other.urls')),
]
