# TuPrimeraPagina-Riveros

Explicacion de funcionalidad:
Tenemos solo 4 botones:
  CoderGym: Solo te lleva a la pagina de inicio.
  Clientes: Metodo POST que sirve para crear a los clientes nuevos y sus nuevos datos
  Actividades: Metodo POST para crear actividades con el cliente que va a asistir, se necesita tener creado un cliente previamente donde con un menu desplegable vas a poderlos. Este tiene como FK el atributo cliente. ACLARACION: de momento las actividades no se pueden duplicar porque se bugea a la hora de marcar asistencias por las FK.
  Asistencias: Metodo POST, aca marcamos que dia que asistio tal cliente a tal actividad. Al igual que el boton anterior, tenemos FK a los clientes como las actividades, un BOOL para marcar presente y un espacio para fecha IMPORTANTE solo permite el formato YYYY-MM-DD por cuestion de la DB.
  Send Feedback: No hace nada, vino en la plantilla y le saque la funcionalidad pero lo deje para que rellene un poco.

Aspecto desde el codigo:
  Al principio puse todo dentro de una aplicacion llamada usuarios porque a decir verdad, no lo pense muy bien, la idea actual es separar cada parte para que tengan su respectivo CRUD y sea mas escalable. Hay varios bugs por cuestiones del modelo como el que no puedo duplicar una actividad y creo que se debe a que no planifique bien desde un principio, tambien debo buscar como corregir el tema de la fecha y si se puede sacar un calendario desde el front para que sea mas facil de marcar asistencia
  El codigo fue con ayuda de chatgpt en parte donde se me complicaron, despues utilice codigo que me creo para guiarme y usar de referencia para continuar de manera no dependiente
  Ya casi al final empece a documentar un poco pero nada.
