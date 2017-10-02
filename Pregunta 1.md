Pregunta 1: Elaborar un documento txt donde se explique 3 principios SOLID que usted considere que no se
cumplen en el c�digo entregado. Se recomienda seguir el formato markdown (ver referencias).

a. Single Responsability (S):
La clase ``` CinePlaneta ``` no esta respetando el principio de Single Responsability puesto que la funciones ``` guardar_entrada ```,
``` listar_peliculas ``` y ``` listar_funciones ``` estan vinculadas entre ellas pero no est�n enfocadas a realizar una funci�n
�nica del cine, adem�s que se crea m�todos innecesarios, este situaci�n tambi�n se presenta con la clase ``` CineStark ```.

b. Open Close (O):
Tambi�n se considera que no se ha cumplido con este principio ya que en caso se quisiera instanciar nuevas peliculas o funciones
estar�amos pr�cticamente en la obligaci�n de cambiar el c�digo donde se crearian (clases ``` CinePlaneta ``` y ``` CineStark ```)

c. Inversi�n de Dependencias (I):
Este principio se esta incumpliendo tambien puesto que las clases Cineplaneta y CineStark dependen fuertemente de la clase Pelicula
(se encuentra acoplados entre si), esta caracter�stica de acoplamiento se puede mostrar cuando se instancia algun objeto de la clase
Pelicula en las clase Cine.