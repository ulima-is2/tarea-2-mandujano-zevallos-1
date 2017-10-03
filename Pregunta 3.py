import sys
import sqlite3

conn = sqlite3.connect('tarea2pregunta3.db')

#definir cursor
cu = conn.cursor()

class crearTodaBD():
    def creates():
        
        cu.execute('''CREATE TABLE
                    IF NOT EXISTS Cines(
                    nombre TEXT NOT NULL)''')

        cu.execute('''CREATE TABLE
                    IF NOT EXISTS Peliculas(
                    pelicula_id INT NOT NULL,
                    nombre TEXT NOT NULL)''')

        cu.execute('''CREATE TABLE
                    IF NOT EXISTS Funciones(
                    idfunc INT NOT NULL,
                    nombrefunc TEXT NOT NULL)''')

        conn.commit()

    def insertCines(cine):
        cu.execute("""INSERT INTO Cines (nombrecine)"
                    VALUES (1, 'CinePlaneta')""")

        cu.execute("""INSERT INTO Cines (nombrecine)"
                    VALUES (2, 'CineStark')""")
        
        conn.commit()


    def insertPeliculas(pelicula):
        cu.execute("""INSERT INTO Peliculas (nombre)
                    VALUES (1, 'IT')""")

        cu.execute("""INSERT INTO Peliculas (nombre)
                    VALUES (2, 'La hora Final')""")
        
        cu.execute("""INSERT INTO Peliculas (nombre)
                    VALUES (3, 'Desaparecido')""")
        
        cu.execute("""INSERT INTO Peliculas (nombre)
                    VALUES (4, 'Deep el Pulpo')""")

        conn.commit()

    def insertFunciones(funcion):
        cu.execute("""INSERT INTO Funciones (idfunc, nombrefunc)"
                    VALUES (1, '19:00'),
                           (1, '20.30'),
                           (1, '22:00'),
                           (1, '21:00'),
                           (1, '20:00'),
                           (1, '23:00'),
                           (1, '16:00')""")
        
        cu.execute("""INSERT INTO Funciones (idfunc, nombrefunc)"
                    VALUES (1, '21:00'),
                           (1, '23.30'),
                           (1, '16:00'),
                           (1, '20.00')""")

        conn.commit()
        cu.close()

#Patron Fachada
class GrupoGlobal:
    def __init__(self):
        self.elementos = []
    
    def add(self, cine, pelicula, pelicula_id, funciones):
        self.elementos.append([cine, Pelicula(pelicula_id, pelicula), funciones])

    def listar_peliculas(self, cine):
        for elem in datos:
            if elem[0].nombre == cine:
                print("{} {}".format(elem[1].id, elem[1].id, elem[1].nombre))

class Entrada:
    def __init__(self, pelicula_id, funcion, cantidad):
        self.pelicula_id = pelicula_id
        self.funcion = funcion
        self.cantidad = cantidad


class Pelicula:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def set_nombre(self, nombre):
        self.nombre = nombre


class Cine:
    def __init__(self, nombre):
        self.nombre = nombre


#Patron Factory
        
class FactorydeCine():
    def obtener_cine(self, nombre_cine):
        if nombre_cine == 'CinePlaneta':
            return CinePlaneta()
        elif nombre_cine == 'CineStark':
            return CineStark()
        else:
            return None

class CinePlaneta:
    def __init__(self):
        peliculaIT = Pelicula(1, 'IT')
        peliculaHF = Pelicula(2, 'La Hora Final')
        peliculaD = Pelicula(3, 'Desparecido')
        peliculaDeep = Pelicula(4, 'Deep El Pulpo')

        peliculaIT.funciones = ['19:00', '20.30', '22:00']
        peliculaHF.funciones = ['21:00']
        peliculaD.funciones = ['20:00', '23:00']
        peliculaDeep.funciones = ['16:00']

        self.lista_peliculas = []
        self.entradas = []

    def listar_peliculas(self):
        return self.lista_peliculas

    def listar_funciones(self, pelicula_id):
        return self.lista_peliculas[int(pelicula_id) - 1].funciones

    def guardar_entrada(self, id_pelicula_elegida, funcion_elegida, cantidad):
        self.entradas.append(Entrada(id_pelicula_elegida, funcion_elegida, cantidad))
        return len(self.entradas)

class CineStark:

    def __init__(self):
        peliculaD = Pelicula(1, 'Desparecido')
        peliculaDeep = Pelicula(2, 'Deep El Pulpo')

        peliculaD.funciones = ['21:00', '23:00']
        peliculaDeep.funciones = ['16:00', '20:00']

        self.lista_peliculas = [peliculaD, peliculaDeep]
        self.entradas = []

    def listar_peliculas(self):
        return self.lista_peliculas

    def listar_funciones(self, pelicula_id):
        return self.lista_peliculas[int(pelicula_id) - 1].funciones

    def guardar_entrada(self, id_pelicula_elegida, funcion_elegida, cantidad):
        self.entradas.append(Entrada(id_pelicula_elegida, funcion_elegida, cantidad))
        return len(self.entradas)

class principal_pantalla():
    #instanciar factory
    factorycine = FactorydeCine()

    grupito = GrupoGlobal()

    grupito.add(factorycine.obtener_cine("CineStark"),
                1, "Deep El Pulpo", ["16:00", "20:00"])

    def opcioneselegir(self):
        terminado = False;
    
        while not terminado:
            print('Ingrese la opción que desea realizar')
            print('(1) Listar cines')
            print('(2) Listar cartelera')
            print('(3) Comprar entrada')
            print('(0) Salir')
            opcion = input('Opción: ')
            
            ###cu.execute('SELECT * FROM Cines WHERE nombrecine = ?')

            #opciones
            if opcion == '1':
                print('********************')
                print('Lista de cines')
                print('1: CinePlaneta')
                print('2: CineStark')
                print('********************')

            elif opcion == '2':
                print('********************')
                print('Lista de cines')
                print('1: CinePlaneta')
                print('2: CineStark')
                print('********************')

                cine = input('Primero elija un cine:')
                if cine == '1':
                    # CinePlaneta
                    cine = CinePlaneta()
                elif cine == '2':
                    cine = CineStark()

                peliculas = cine.listar_peliculas()
                print('********************')
                for pelicula in peliculas:
                    print("{}. {}".format(pelicula.id, pelicula.nombre))
                print('********************')

            elif opcion == '3':
                print('********************')
                print('COMPRAR ENTRADA')
                print('Lista de cines')
                print('1: CinePlaneta')
                print('2: CineStark')
                print('********************')
                cine = input('Primero elija un cine:')
            
                if cine == '1':
                    cine = CinePlaneta()
                elif cine == '2':
                    cine = CineStark()

                peliculas = cine.listar_peliculas()

                pelicula_elegida = input('Elija pelicula:')

            
                #pelicula = obtener_pelicula(id_pelicula)
                print('Ahora elija la función (debe ingresar el formato hh:mm): ')

                funcion_elegida = input('Funcion:')
                cantidad_entradas = input('Ingrese cantidad de entradas: ')
                codigo_entrada = cine.guardar_entrada(pelicula_elegida, funcion_elegida, cantidad_entradas)
                print('Se realizó la compra de la entrada. Código es {}'.format(codigo_entrada))
                
            elif opcion == '0':
                terminado = True
            else:
                print(opcion)

class cargarprincipal():
    prin = principal_pantalla()

    prin.opcioneselegir()

if __name__ == '__main__':
    cargarprincipal()
