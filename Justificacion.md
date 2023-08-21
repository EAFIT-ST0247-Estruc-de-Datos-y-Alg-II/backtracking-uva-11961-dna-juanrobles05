# BACKTRACKING-UVA-11961-DNA-SOLUTION

1. El lenguaje de programación utilizado y por qué fue seleccionado.

>Python 3.11.2, escogí este lenguaje de programacion ya que gracias al curso de datos y algoritmos 1 desarrolle un buen nivel en este mismo ademas de ser un lenguaje sumamente sencillo en sintaxis comparado con otros por otro lado el hecho de que este lenguaje se haya vuelto un lenguaje tan popular implica que tenga mucha informacion de la cual precindir en caso de dificultades con el codigo.

2. Descripción del algoritmo en pseudocódigo. ¿Por qué funciona?

>El algoritmo toma tres parametros `N`(la longitud de la secuencia de ADN), `secuencia`(la secuencia de ADN original) y las `mutaciones_requeridas`(el numero de mutaciones que se pueden realizar o como lo llaman en el enunciado K) luego creamos un set() llamado mutaciones para almacenar las secuencias mutadas y asegurarnos de que sean unicas.
>definimos una funcion interna llamada `generar_combinaciones` que recibe tres parametros `secuencia_actual` (la secuencia actual que se esta mutando), mutaciones_restantes (el numero de mutaciones que aun se debe aplicar a la secuencia) e `index` (el indice en el que se comenzara a realizar las mutaciones) en esta funcion si `mutaciones_restantes` es igual a 0 entonces se agrega la `secuencia_actual` al conjunto de `mutaciones` y retorna. Luego utilizamos 2 ciclos for anidados para iterar atraves de los indices y las letras "'A','C','G','T'". Para cada letra creamos una nueva secuencia mutada llamada `nueva_secuencia` esto lo hacemos tomando todo lo que esta antes del indice luego insertamos la letra en la pocision i y le agregamos todo lo que va despues del indice i. despues llamamos recursivamente a la funcion `generar_combinacion` con la `nueva_secuencia`, `mutaciones_restantes - 1` y `i + 1` para avanzar al siguiente, cuando terminamos llamamos nuevamente a la funcion `generar_combinaciones` con la `secuencia` original, `mutaciones_requeridas` y el indice inicial en 0 para comenzar a generar las mutaciones. Finalmente luego de haber generado todas las mutaciones ordenamos `mutaciones` y devolvemos la lista ordenada.
>El programa principal lee los casos de prueba `T` y para cada caso de prueba lee la longitud `N`, el numero de mutaciones`K` y la secuencia de ADN `secuencia` para la `N` y la `K` utilizamos la funcion map con la funcion int para asegurarnos de que sean int. Por ultimo llamamos a la funcion `secuenciador_adn` con los datos leidos anteriormente y luego imprimimos la cantidad de mutaciones y cada mutacion en la lista resultante.

3. Descripción del mecanismo de backtracking: ¿Cuál es el criterio que utiliza para definir que no tiene sentido continuar con la exploración de la solución y que se debe deshacer la última decisión tomada?

>El criterio que se utiliza es formado apartir de lo siguiente: exploramos todas las combinaciones combinando cada letra  en cada posicion de la secuencia. luego para deshacer la ultima decision tenemos la funcion `generar_combinaciones` de manera recursiva en donde la ultima decision tomada es representada por la ultima llamada recursiva. Una vez se han completado todas las combinaciones posibles desde un punto especifico se regresa a ese punto y se continua con la proxima combinacion y por ultimo para saber donde parar utilizamos tambien la funcion `generar_combinaciones` ya que en esta cuando las `mutaciones_restantes` llegan a 0 se agrega la `secuencia_actual` a la lista `mutaciones`.

4. ¿Cómo calcula el número de permutaciones que hay en la respuesta?

>El numero de permutacuiones que hay en la respuesta se basa en como se generan las combinaciones debido a que en la funcion `generar_combinaciones` en cada llamada recursiva, se disminuye el valor de `mutaciones_restantes` en 1. Esto significa que en cada nivel de recursion exploramos tolas las combinaciones posibles y ya que nos aseguramos de explorar todas las combinaciones pero unicamente almacenar las que son unicas simplemente miramos el tamaño de `mutaciones` y esto nos dara el numero total de permutaciones.

5. ¿Cómo cambiaría el algoritmo si en lugar de preguntar por todas las mutaciones preguntara solo por una? Justifique su respuesta.

>Se eliminaria la recursion y se simplificaria el codigo ya que no queremos conocer todas las combinaciones posibles por lo que no es necesario explorarlas sino que simplemente preguntamospor una mutacion y la realizamos directamente en la posicion indicada.

7. La definición de cada función. Siguiendo la línea propuesta en CORBA[^1] se deben incluir los siguientes elementos:
    * Funcion: `secuenciador_adn(N, secuencia, mutaciones_requeridas)`
    * Parámetros que recibe:
        * `N` (int): Longitud de la secuencia de ADN.
        * `secuencia` (str): Secuencia de ADN original.
        * `mutaciones_requeridas` (int): Número de mutaciones que se deben realizar.
    * Tipo de dato que retorna:
        * `set`: Conjunto que contiene las combinaciones de ADN mutadas.
    * Excepciones que produce:
        * Ninguna.
    * Descripción corta de qué hace:
        >Esta función genera todas las combinaciones posibles de ADN mutadas con el número de mutaciones requeridas en la secuencia original. Utiliza la función interna generar_combinaciones para explorar todas las combinaciones posibles de mutaciones.


    * Funcion: `generar_combinaciones(secuencia_actual, mutaciones_restantes, index)`
    * Parámetros que recibe:
        * `secuencia_actual` (str): La secuencia de ADN actual con mutaciones realizadas hasta el momento.
        * `mutaciones_restantes` (int): El número de mutaciones restantes que se deben realizar.
        * `index` (int): El índice actual de la secuencia en el que se está evaluando la mutación
    * Tipo de dato que retorna:
        * Ninguno (void).
    * Excepciones que produce:
        * Ninguna.
    * Descripción corta de qué hace:
        >Esta función realiza una búsqueda exhaustiva para generar todas las combinaciones posibles de mutaciones en la secuencia actual. Comienza en el índice index y reemplaza la letra en esa posición con 'A', 'C', 'G' y 'T'. Luego, llama recursivamente a la función para continuar evaluando las mutaciones en las posiciones siguientes.


| Nombre de la variable | Tipo de dato | Uso                                       | Visibilidad | Ciclo de vida                |
|-----------------------|--------------|-------------------------------------------|-------------|------------------------------|
| N                     | int          | Longitud de la secuencia de ADN.          | Local       | Desde la entrada hasta el fin de la función `secuenciador_adn`.                  |
| secuencia             | str          | Secuencia de ADN original.                | Local       | Desde la entrada hasta el fin de la función `secuenciador_adn`.                  |
| mutaciones_requeridas | int          | Número de mutaciones requeridas.          | Local       | Desde la entrada hasta el fin de la función `secuenciador_adn`.                  |
| mutaciones            | set          | Conjunto que almacena las combinaciones de ADN mutadas. | Local   | Desde la creación hasta el fin de la función `secuenciador_adn`.                 |
| letra                 | str          | Representa las letras 'A', 'C', 'G' y 'T'. | Local       | En el bucle interno de la función `generar_combinaciones`.                         |
| nueva_secuencia       | str          | Secuencia resultante después de la mutación. | Local  | En el bucle interno de la función `generar_combinaciones`.                         |
| T                     | int          | Número de casos de prueba.                | Local       | Desde la entrada hasta el fin del ciclo `for` principal.                  |                  |
| mutacion              | str          | Una combinación mutada de ADN.             | Local       | En el bucle interno después de llamar a la función `secuenciador_adn`.          |