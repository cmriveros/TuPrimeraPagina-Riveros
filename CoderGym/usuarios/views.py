from django.shortcuts import render
from usuarios.models import Cliente
from usuarios.forms import ClienteFormulario

# Create your views here.

def crear_cliente(request):
    
    if request.method == "POST":
        nuevo_formulario = ClienteFormulario(request.POST)

        if nuevo_formulario.is_valid():
            informacion = nuevo_formulario.cleaned_data
            nuevo_cliente = Cliente(
                    nombre=informacion["nombre"],
                    email=informacion["email"],
                    edad=informacion["edad"],
                    fecha_ingreso=informacion["fecha_ingreso"]
                    )
                
            nuevo_cliente.save()
            return render(request, 'index.html')
    else:
        nuevo_formulario = ClienteFormulario()
        return render(request, 'clientes_forms.html', {"formulario": nuevo_formulario})
  
# def asistencia(request):
#     if request.method == "POST":
#             form = AsistenciasFormulario(request.POST)
            
#             if form.is_valid():
#             # Obtener desde el formulario
#                 nombre_cliente = form.cleaned_data['cliente']
#                 action= form.cleaned_data['actividad']

#             # Obtener la instancia
#                 cliente_instance = Cliente.objects.get(nombre=nombre_cliente)
#                 actividad_instance = Actividad.objects.get(nombre_actividad=action)

#             # Crear la instancia de Actividad con la instancia de Cliente
#                 actividad = Asistencia(
#                 cliente=cliente_instance,
#                 actividad=actividad_instance,
#                 fecha=form.cleaned_data['fecha'],
#                 asistio=form.cleaned_data['asistio']
#             )

#             # Guardar la actividad en la base de datos
#             actividad.save()
#             return render(request, 'index.html')
#     else:
#             form = AsistenciasFormulario()

#     return render(request, 'asistencias_forms.html', {"form": form})


