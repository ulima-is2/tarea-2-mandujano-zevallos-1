### Sustento de elección de patrones:

**Patrón Factory**: se decidio emplear este patrón puesto que los dos cines (``` CinePlaneta ``` y ``` CineStark ```)
pueden ser implementados como clases hijas por el principio de cohesión además que heredan sus
mismas funciones.
***
**Patrón Fachada**: este patrón lo utilizamos con el objetivo de que el cliente del cine solamente se
comunique con una clase Gestor (``` GestorGlobal ```) y no con todos los métodos más estructurados de este,
con esto logramos darle al cliente una plataforma sencilla, nos ayuda a reducir las dependencias
entre padre e hijos.
***
**Patrón Composite**: finalmente este patrón se puede implementar ya que las clases ``` Cine ```, ``` Peliculas ``` y
``` Funciones ``` se pueden estructurar como árbol para lograr realizar alguna operación, por ejemplo el
monto total de ganancia de las entradas.
