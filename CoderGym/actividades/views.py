from django.shortcuts import render
from actividades.models import Actividad
from actividades.forms import ActividadesFormulario
from usuarios.models import Cliente

# Create your views here.

def nueva_actividad(request):
    if request.method == "POST":
            form = ActividadesFormulario(request.POST)
            
            if form.is_valid():
                actividad = Actividad(
                precio=form.cleaned_data['precio'],
                nombre_actividad=form.cleaned_data['nombre_actividad'],
                descripcion=form.cleaned_data['descripcion']
            )

            # Guardar la actividad en la base de datos
            actividad.save()
            return render(request, 'index.html')
    else:
            form = ActividadesFormulario()

    return render(request, 'actividades_forms.html', {"form": form})