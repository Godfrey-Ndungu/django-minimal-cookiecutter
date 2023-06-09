from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularRedocView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
