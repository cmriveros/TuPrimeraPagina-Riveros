from django import forms
from .models import Cliente, Actividad

class ClienteFormulario(forms.Form):
    nombre = forms.CharField()
    email = forms.EmailField()
    edad = forms.IntegerField()
    fecha_ingreso = forms.DateField()

class ActividadesFormulario(forms.Form):
    clientes = Cliente.objects.all()
    opciones_clientes = [(n.nombre, n.nombre) for n in clientes]

    cliente = forms.ChoiceField(choices=opciones_clientes)
    precio = forms.IntegerField()
    nombre_actividad = forms.CharField()
    descripcion = forms.CharField(widget=forms.Textarea, required=False)

class AsistenciasFormulario(forms.Form):
    clientes = Cliente.objects.all()
    opciones_clientes = [(n.nombre, n.nombre) for n in clientes]

    actividades = Actividad.objects.all()
    opciones_actividad = [(n.nombre_actividad, n.nombre_actividad) for n in actividades]

    cliente = forms.ChoiceField(choices=opciones_clientes)
    actividad = forms.ChoiceField(choices=opciones_actividad)
    fecha = forms.DateField()
    asistio = forms.BooleanField()