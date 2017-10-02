## Pregunta 1:

## a. Single Responsability (S):
La clase ``` CinePlaneta ``` no esta respetando el principio de Single Responsability puesto que la funciones ``` guardar_entrada ```,
``` listar_peliculas ``` y ``` listar_funciones ``` estan vinculadas entre ellas pero no están enfocadas a realizar una función
única del cine, además que se crea métodos innecesarios, este situación también se presenta con la clase ``` CineStark ```.

## b. Open Close (O):
También se considera que no se ha cumplido con este principio ya que en caso se quisiera instanciar nuevas peliculas o funciones
estaríamos prácticamente en la obligación de cambiar el código donde se crearian (clases ``` CinePlaneta ``` y ``` CineStark ```).

## c. Inversión de Dependencias (I):
Este principio se esta incumpliendo también puesto que las clases ``` CinePlaneta ``` y ``` CineStark ``` dependen fuertemente de la clase 
Pelicula (se encuentra acoplados entre sí), esta característica de acoplamiento se puede mostrar cuando se instancia algun objeto de la clase Pelicula en las clase Cine.
