"""
Нащ Основной Маршрутизатор
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Путь До Админ Панели
    path('', include("app.urls"))
]
