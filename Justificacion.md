# BACKTRACKING-UVA-11961-DNA-SOLUTION

1. El lenguaje de programación utilizado y por qué fue seleccionado.

>Python 3.11.2, escogí este lenguaje de programacion ya que gracias al curso de datos y algoritmos 1 desarrolle un buen nivel en este mismo ademas de ser un lenguaje sumamente sencillo en sintaxis comparado con otros por otro lado el hecho de que este lenguaje se haya vuelto un lenguaje tan popular implica que tenga mucha informacion de la cual precindir en caso de dificultades con el codigo.

2. Descripción del algoritmo en pseudocódigo. ¿Por qué funciona?
>El algoritmo toma tres parametros 'N'(la longitud de la secuencia de ADN), 'secuencia'(la secuencia de ADN original) y las 'mutaciones_requeridas'(el numero de mutaciones que se pueden realizar o como lo llaman en el enunciado K) luego creamos un set() llamado mutaciones para almacenar las secuencias mutadas y asegurarnos de que sean unicas.
>definimos una funcion interna llamada 'generar_combinaciones' que recibe tres parametros 'secuencia_actual' (la secuencia actual que se esta mutando), mutaciones_restantes (el numero de mutaciones que aun se debe aplicar a la secuencia) e 'index' (el indice en el que se comenzara a realizar las mutaciones) en esta funcion si
3. Descripción del mecanismo de backtracking: ¿Cuál es el criterio que utiliza para definir que no tiene sentido continuar con la exploración de la solución y 3. se debe deshacer la última decisión tomada?
4. ¿Cómo calcula el número de permutaciones que hay en la respuesta?
5. ¿Cómo cambiaría el algoritmo si en lugar de preguntar por todas las mutaciones preguntara solo por una? Justifique su respuesta.
6. La definición de las clases utilizadas, en caso de haberlo hecho. Para cada clase debe definirse cuál es el dominio, i.e. los valores que son válidos, y cuáles son los métodos. Los métodos deben ser definidos siguiendo la misma estructura que se propone a continuación para las funciones.
7. La definición de cada función. Siguiendo la línea propuesta en CORBA[^1] se deben incluir los siguientes elementos:
    * Nombre de la función
    * Parámetros que recibe
    * Tipo de dato que retorna
    * Excepciones que produce
    * Descripción corta de qué hace
8. La descripción de las variables. Se debe realizar una tabla que tenga la siguiente información:
    * Nombre de la variable
    * Tipo de dato que almacena
    * Para qué se utiliza
    * Visibilidad, es decir, quiénes tienen acceso a esa variable
    * Ciclo de vida, es decir, cuándo se crea y cuándo se destruye
    *Nota:* No es necesario incluir las variables temporales, como por ejemplo las utilizadas en los ciclos.
9. Se revisará también la calidad del código. Algunos ejemplos de cosas que se penalizan:
    * Utilizar variables globales
    * Incluir en los ciclos cálculos que no cambian en cada iteración
    * Nombres arbitrarios de variables o funciones (aleatorios o sin ninguna relación con la semántica de la variable o la función)
