from django.urls import path
from actividades.views import nueva_actividad

urlpatterns = [
    path('nueva_actividad/', nueva_actividad, name='nueva actividad'),
]