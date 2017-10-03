Sustento de elecci�n de patrones:

Patr�n Factory: se decidio emplear este patr�n puesto que los dos cines (``` CinePlaneta ``` y ``` CineStark ```)
pueden ser implementados como clases hijas por el principio de cohesi�n adem�s que heredan sus
mismas funciones.

Patr�n Fachada: este patr�n lo utilizamos con el objetivo de que el cliente del cine solamente se
comunique con una clase Gestor (``` GestorGlobal ```) y no con todos los m�todos m�s estructurados de este,
con esto logramos darle al cliente una plataforma sencilla, nos ayuda a reducir las dependencias
entre padre e hijos.

Patr�n Composite: finalmente este patr�n se puede implementar ya que las clases ``` Cine ```, ``` Peliculas ``` y
``` Funciones ``` se pueden estructurar como �rbol para lograr realizar alguna operaci�n, por ejemplo el
monto total de ganancia de las entradas.