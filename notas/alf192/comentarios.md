## Comentarios de Favio

* Nota 1 (`n01alf192.tex`)

  - [x] Agrega ejemplos para cada operacion en la sección 6.

* Nota 2 (`n02alf192.tex`)

  - [x] Agrega ejemplos específicos después de la def. 2, y luego usa esos mismos
para dar ejemplos de la def. 3

  - [x] Da ejemplos de la def. 4, es decir verifica algunas igualdades de expresiones regulares usando la def. 4

  - [x] Seccion 3: da ejemplos del uso de propiedades de cerradura para verificar que un lenguaje es regular.

  - [x] Seccion 4: pon ligas y/o bibliografía a las aplicaciones y busca algunas más

* Nota 3 (`n03alf192.tex`)

  - [ ] Agrega 3 ejemplos de AFD en toda la nota, definiendo primero con la tabla, luego con el diagrama de estados y el lenguaje de aceptación.

  - [x] Agrega el diagrama para el ejemplo de la seccion 3.1 y pon otros ejemplos; pon otros ejemplos en la sección 3.2

  - [x] Pon otros ejemplos en la 3.3, tanto las tablas como los diagramas, uno por cada operación: union, intersección, diferencia.

---

## Comentarios de Ángel

Generé unos [pdf's](revision-pdf/) con unas anotaciones para que me diga si le 
pareció bien o necesita que modifique lo que agregué.

### Nota 1

Para la Nota 1, utilicé **Introduction to Automata Theory, Languages, and Computation By Hopcroft, Motwani, & Ullman (2nd, Second Edition)** de la página 83-85. Para la parte de los ejemplos 
también utilicé esta [presentación](resources/RegularExpressions.ppt).

### Nota 2

Para la Nota 2, utilicé [James A. Anderson - Automata Theory with Modern Applications -Cambridge University Press (2006)](resources/James%20A.%20Anderson%20-%20Automata%20Theory%20with%20Modern%20Applications%20-Cambridge%20University%20Press%20(2006).pdf) en la página 25 para la parte de denotaciones. 

En la definición 4 para demostrar que dos expresionees regulares son equivalentes use esta
[diapositiva](resources/unit4_10.pdf) página 13 y 14.

Para demostrar las partes de la cerradura utilicé esta [diapositiva](resources/lec05.pdf).

El ejemplo de expresión regular lo encontré 
[aquí](https://www.digitalocean.com/community/tutorials/using-grep-regular-expressions-to-search-for-text-patterns-in-linux).

En la nota 2 no demostré que el complmento de un lenguaje es cerrado  solo usando 
expresiones regulares porque no supe como y las [formas que vi](https://math.stackexchange.com/questions/2018315/complement-of-regular-language-is-regular), 
primero debía mostrar que es cerrado bajo homomorfismos y luego usar eso.
Lo más sencillo que encontré fue lo común, con el autómata. Entonces por eso escribí 
**pendiente**.

### Nota 3

En la nota 3, en la parte de poner los ejemplos de diseño por autómata por 
complemento, utilicé estas [diapositivas](resources/Small13.pdf)

En la parte donde puse `TODO: PONER AQUÍ EL AUTOMATA DEL EJEMPLO DE ARRIBA`, hago 
ese autómata yo, o descomento el que ya está?

Para los ejemplos de modularización utilicé está [diapositiva](resources/lecture-3.pdf). 

### Fuentes

https://cs.fit.edu/~dmitra/FormaLang/Lectures/RegularExpressions.ppt

https://www.cs.colorado.edu/~astr3586/courses/csci3434/lec05.pdf

http://www1.idc.ac.il/toky/automata/lectures/unit4_10.pdf

https://www.digitalocean.com/community/tutorials/using-grep-regular-expressions-to-search-for-text-patterns-in-linux

https://web.stanford.edu/class/archive/cs/cs103/cs103.1142/lectures/13/Small13.pdf

https://www.andrew.cmu.edu/user/ko/pdfs/lecture-3.pdf
