
# Bitácora - Actividad 1

# Estructura para almacenar las columnas
Para almacenar la información de las columnas entre las colecciones vistas en clases se eligio utilizar un diccionario llamado `COLUMNAS` formada a su vez por diccionarios que contendran el tipo de dato y su porcentaje de completitud.
Si bien para los objetivos del problema planteado, podrian haberse utilizado listas se eligio este tipo de estructura por la facilidad en la consulta de los datos. Se explota la caracteristica de la consulta mediante clave-valor que proporciona los diccionarios, sin conocer la posicion de cada dato como exige otras estructuras. Se descarto las Tuplas porque se imagino que deberian tener una flexibilidad que al ser estructuras no modificables no podian darnos, ademas del mismo problema de las listas que serian mas complicados al momento de la consulta. 
Asimismo, para completar los valores de la completitud de las variables, se usaron aleatoriamente entre 0 y 100 pero habiendose probado las funciones con distintos valores bajo y superior a los limites.

# ROLES
## Estructura para almacenar los roles

Para almacenar la configuración de los roles también decidí utilizar un diccionario. Cada rol funciona como una clave y tiene asociada su configuración.
Sin embargo, dentro de cada rol utilicé una lista para guardar las columnas de interés, ya que en este caso solamente necesito almacenar los nombres de las columnas que corresponden a ese rol. Se utilizaron listas porque si luego necesitamos eliminar o agregar datos para el mismo rol, sera mas facil bajo esta estructura.
Asimismo, cada rol almacena un criterio de ordenamiento y la forma de ordenarlo, como tambien un porcentaje minimo de completitud.



## Funciones
En un comienzo se trabajo con una unica funcion lo que se hizo complicado de compilar y en vistas de la version final un uso por demas de la funciones anonimas lambda. Se dividio la primer funcion, generar informe en otras funciones que seran usadas para esta funcion madre.

`filtrar_columnas()` se encarga de seleccionar las columnas que cumplen con el mínimo de completitud del rol. Se utiliza la funcion filter.

`ordenar_columnas()` se encarga de ordenar las columnas según el criterio y la forma de orden configurados. Si aparece un criterio no contemplado esta funcion nos va a visar, como puede ser ordenar por "promedio".

`mostrar_columnas()` se encarga de mostrar el nombre, tipo y completitud de las columnas.

Finalmente, `generar_informe()` coordina las funciones anteriores según el rol solicitado. Se utiliza el valor por defecto None que nos va a permitir ordenar si no nos asignan ningun rol por complitud.



## Problemas encontrados y soluciones
Uno de los problemas que aparecio fue al intentar de utilizar el notebook para probar las funciones y no lograba que la reconozca. Esto me freno reiteradas ocasiones hasta entender que el problema es que ademas de guardar las nuevas funciones tenia ue reiniciar el kernel del notebook.

## Modificaciones Solicitadas
De acuerdo a las modificaciones que se pidieron en la evaluacion se agrego el nuevo rol economista, configurando sus columnas solicitadas, orden ascendente y el minimo de 90 % de completitud. Al probarlo se eliminaron las columnas CAT_OCUP, ITF y GDECCFR.

También se incorporo la nueva columna `CH04`, de tipo `int` y con 95% de completitud, y la agregué a las columnas de interés del rol `investigador`. Al ejecutar el informe comprobé que aparece correctamente ordenada según su porcentaje de completitud.
