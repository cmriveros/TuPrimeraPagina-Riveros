from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.EmailField()
    edad = models.IntegerField()
    fecha_ingreso = models.DateField()

class Actividad(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="actividades")
    precio = models.IntegerField()
    nombre_actividad = models.CharField(max_length=30)
    descripcion = models.TextField()

class Asistencia(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="asistencia")
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    fecha = models.DateField()
    asistio = models.BooleanField(default=False)
