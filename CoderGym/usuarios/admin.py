from django.contrib import admin
from usuarios.models import Cliente, Actividad, Asistencia
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Actividad)
admin.site.register(Asistencia)