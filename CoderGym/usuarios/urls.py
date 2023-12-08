from django.urls import path
from usuarios.views import crear_cliente, nueva_actividad, asistencia

urlpatterns = [
    path('crear_cliente/', crear_cliente, name='crear cliente'),
    path('nueva_actividad/', nueva_actividad, name='nueva actividad'),
    path('asistencia/', asistencia, name='asistencia')
]