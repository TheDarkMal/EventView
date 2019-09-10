from django.urls import path
from .views import (cargar_inicio)

urlpatterns = [
    path('', cargar_inicio, name = 'inicio'),
]