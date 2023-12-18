# TuPrimeraPagina-Riveros

## Descripción de Funcionalidad:

Este proyecto presenta una interfaz con cuatro botones principales:

1. **CoderGym:**
    - Redirige a la página de inicio.

2. **Clientes:**
    - Método POST para crear nuevos clientes y sus datos asociados.

3. **Actividades:**
    - Método POST para crear actividades con el cliente correspondiente.
    - Se requiere haber creado previamente un cliente, y se selecciona a través de un menú desplegable.
    - Nota: Actualmente, no se pueden duplicar actividades debido a problemas con las claves foráneas (FK) al marcar asistencias.

4. **Asistencias:**
    - Método POST para registrar la asistencia de un cliente a una actividad.
    - Al igual que el botón anterior, implica el uso de claves foráneas para clientes y actividades.
    - Incluye un campo booleano para marcar la presencia y un espacio para la fecha (formato YYYY-MM-DD).

5. **Send Feedback:**
    - Actualmente no tiene funcionalidad. Se dejó en la plantilla para futuras mejoras.

## Aspectos del Código:

- Inicialmente, todas las funciones se encontraban dentro de una aplicación llamada 'usuarios'. Sin embargo, se planea reorganizar el código para que cada parte tenga su propio CRUD, facilitando la escalabilidad.

- Existen varios bugs relacionados con el modelo, como la imposibilidad de duplicar actividades. Se sospecha que estos problemas surgieron debido a una planificación inicial insuficiente.

- Se está considerando la corrección del formato de la fecha y la posible incorporación de un calendario en el frontend para facilitar el registro de asistencias.

- El código se desarrolló con la ayuda de ChatGPT en áreas complicadas. Posteriormente, se utilizaron fragmentos de código creados como referencia para continuar de manera más independiente.

- La documentación del código se inició hacia el final del desarrollo, aunque aún es limitada. Se planea mejorar la documentación en futuras iteraciones del proyecto.
