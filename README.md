[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/B0JCyXFX)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=11549647)
# UVA-11961-DNA
## Primera Práctica: Algoritmos de Fuerza Bruta y Back Tracking
Problema de backtracking para generar mutaciones de ADN

## Objetivo
El objetivo de esta práctica es resolver un problema utilizando backtracking. Como recordarán, el backtracking es una optimización de la fuerza bruta en la cual, cuando una decisión no conduce a una solución válida, se deshacen los pasos y se cambia la decisión. Es una optimización de un enfoque de fuerza bruta cuando se puede determinar que no hay solución válida con un subconjunto de la solución (usualmente un prefijo), así que al deshacer la decisión se evita evaluar múltiples combinaciones.

## Problema

El problema a resolver se denomina *ADN*. El enunciado lo encuentra anexo y también lo pueden consultar acá: [Online Judge - 11961 DNA](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=229&page=show_problem&problem=3112). Deben implementar la solución en cualquier lenguaje de programación aceptado por el juez en línea de UVA:

- ANSI C 5.3.0 - GNU C Compiler with options: -lm -lcrypt -O2 -pipe -ansi -DONLINE_JUDGE
- JAVA 1.8.0 - OpenJDK Java
- C++ 5.3.0 - GNU C++ Compiler with options: -lm -lcrypt -O2 -pipe -DONLINE_JUDGE
- PASCAL 3.0.0 - Free Pascal Compiler
- C++11 5.3.0 - GNU C++ Compiler with options: -lm -lcrypt -O2 -std=c++11 -pipe -DONLINE_JUDGE
- PYTH3 3.5.1 - Python 3

### Traducción del enunciado

Alan estaba realizando sus prácticas en la facultad de Química. Al principio las prácticas parecían fáciles. Un día, el decano de la Facultad de Química le encomendó una tarea. Alan debía realizar un modelado de ADN y proteínas utilizando un kit de software gratuito OpenEye. Como Alan, al igual que todos los programadores, es muy perezoso, le gustaría utilizar el computador todo lo posible. Así que ahora tiene que generar todas las mutaciones posibles del ADN y compartirlas con el software OpenEye. Alan decidió utilizar un computador no sólo para el software OpenEye, sino también para generar mutaciones. Al principio de las prácticas, Alan estudió un poco de química, por lo que sabe que el ADN consta de 4 elementos (adenina, guanina, citosina y timina) que pueden describirse como una secuencia de cuatro letras, es decir, GATCC. La K-ésima mutación de la secuencia inicial de ADN de longitud N se denomina una secuencia que puede producirse sustituyendo (posiblemente al mismo nucleótido) exactamente K elementos de la secuencia, es decir, GAT es la 1ª mutación de GGT y la 2ª mutación de TTT. Alan recibe la secuencia inicial de ADN y la máxima potencia de sus posibles mutaciones. ¿Puedes producir todas las posibles secuencias de ADN mutadas para Alan?

## Evaluación

La evaluación está organizada de la siguiente manera:

20% - El programa debe pasar todos los casos de prueba de udebug [uDebug - UVA 11961 DNA ](https://www.udebug.com/UVa/11961). Recuerden que si se registran en udebug, tienen acceso a sugerencias sobre el problema.
40% - El programa debe para los casos de prueba del onlinejudge de UVA [https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=21&page=show_problem&problem=1891](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=229&page=show_problem&problem=3112)
40% - La explicación de la solución utilizada y la calidad del código. Esto incluye:
1. El lenguaje de programación utilizado y por qué fue seleccionado.
2. Descripción del algoritmo en pseudocódigo. ¿Por qué funciona?
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
    
[^1]: CORBA es un acrónimo que quiere decir _Common Object Request Broker_ y fue propuesto en los 90s por el _Object Management Group_. Es un estándar para objetos distribuidos que continua en desarrollo permanente. En la página [http://www.ciaranmchale.com/corba-explained-simply/](http://www.ciaranmchale.com/corba-explained-simply/) encuentran una descripción detallada del estándar. Si bien es un tema avanzado que tiene que ver son la integración de sistemas heterogéneos, los conceptos que allí se presentan son muy importantes.
