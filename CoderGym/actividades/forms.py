from django import forms

class ActividadesFormulario(forms.Form):
    nombre_actividad = forms.CharField()
    precio = forms.IntegerField()
    descripcion = forms.CharField(widget=forms.Textarea, required=False)