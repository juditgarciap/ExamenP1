#crear tabla hash vacia
from sqlite3 import DateFromTicks


def crear_tabla (tamanio):
    tabla = [None] * tamanio
    return tabla


#devuelve cantidad de elementos de la tabla 
def cantida_elementosn(tabla):
    return len(tabla)- tabla.count(None)

def cantidad_elementos (tabla):
    return sum(len(lista) for lista in  tabla if lista is not None)

#determina la posicion del dato en la tabla
def funcion_hash (dato, tamanio_tabla):
    return len(str(dato).strip())% tamanio_tabla


#agregar un elemnto a la tabla encadenada
def agregar(tabla,dato):
    posicion = funcion_hash(dato, len(tabla))
    if (tabla[posicion] is None) :
        tabla [posicion] = dato

    else:
        print ('se produjo una colision')
#ejecutar funcion de sondeo para reubicar elento

#determina si un elemento  existe en la tabla  y determina su posicion
def buscar (tabla,buscado):
    pos = None
    posicion = funcion_hash(buscado, len(tabla))
    if(tabla[posicion]is not None):
        if (buscado== tabla[posicion]):
            pos=posicion
        
        else:
            print ('aplicar funcion sondeo')
    return pos

#quitar un elemto de la tabla cerrada si existe
def quitar(tabla,dato):

    dato = None
    posicion = funcion_hash (dato, len (tabla))
    if (tabla[posicion] is not None):

        if (dato == tabla[posicion]):
            dato = tabla[posicion]
            tabla[posicion] = None

        else:
            print("Aplicar funcion de sondeo")
            """Para determinar si esta en otra posicion y quitarlo"""

    return dato


