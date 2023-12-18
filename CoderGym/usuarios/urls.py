from django.urls import path
from usuarios.views import crear_cliente

urlpatterns = [
    path('crear_cliente/', crear_cliente, name='crear cliente'),
    # path('asistencia/', asistencia, name='asistencia')
]