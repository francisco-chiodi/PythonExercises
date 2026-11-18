"""
La Agencia TurisTour necesita un programa para gestionar la venta de paquetes en una agencia de viajes. Por cada
Paquete vendido se conoce:
• código (cadena de 5 caracteres alfanuméricos),
• destino (cadena),
• aerolínea (entero entre 1 y 5. 1-Fly Airways, 2-AED te da Alas, 3-Cielos Binarios, 4-Al algoritmo y más allá, 5-
O(n)),
• categoría del hotel reservado para el pasajero (entero entre 1 y 6: 1-Hostel, 2-Económico, 3-3 Estrellas, 4-4
Estrellas, 5-5 Estrellas, 6-Resort),
• precio del paquete completo (valor flotante mayor que 0),
• comentarios del cliente (cadena finalizada en “.” con palabras separadas por 1 espacio).
Sobre la generación de los datos aleatorios
La clase que se pide desarrollar debe llamarse Paquete. El programa debe incluir al menos dos módulos: uno para la
clase y otro para el desarrollo del menú y sus opciones. El módulo del menú debe llamarse principal.py. A continuación
sigue un fragmento de código listo para copiar y pegar en su parcial. Cópielo y péguelo tal cual como se ve, al inicio del
módulo en el que desarrollará el menú:
from random import *
seed_set = False
def generar_aleatorio():
 global seed_set
 if not seed_set:
 seed(1211)
 seed_set = True
 destinos = ["París", "Nueva York", "Tokio", "Londres", "Roma"]
 comentarios = [
 "¡Una experiencia inolvidable! Muy recomendado.",
 "Excelente servicio y comodidad.",
 "Muy recomendable para familias.",
 "Perfecto para una escapada romántica.",
 "Buena relación calidad precio."
 ]
 # Generación de cada variable necesaria
 codigo = ''.join(choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(5))
 destino = choice(destinos)
 aerolinea = randint(1, 5)
 categoria = randint(1, 6)
 precio = round(randint(100, 10000) + random(), 2)
 comentario = choice(comentarios)
 # Crear y retornar acá un nuevo objeto de la clase Paquete con los valores generados (marcados en rojo en el modelo)
La función generar_aleatorio() debería devolver un nuev Paquete con los valores generados por el código que copió y
pegó. Lo único que debe hacer al final de esa función es retornar un nuevo objeto del tipo Paquete inicializado con los
valores que se generan en la misma función (reemplace el comentario verde de la última línea de la función por ese
return).

Requerimientos
Desarrollar un programa controlado por menú de opciones para cumplir con cada uno de los siguientes apartados. El
mensaje para la selección de una opción debe ser el siguiente:
opcion = int(input("Ingrese opción: "))
Opción 1: Cargar en un arreglo n objetos del tipo Paquete, de tal forma que sus elementos se mantengan ordenados, en
todo momento, por precio de venta de forma ascendente (usar exclusivamente inserción ordenada con búsqueda
binaria, y genere en forma aleatoria los datos de cada objeto con la función generar_aleatorio() que se le ha provisto).
Cada vez que se ejecute esta opción, el vector debe iniciar vacío (en otras palabras, cada vez que se ejecute la opción, se
crea un nuevo vector vacío)
Resultados esperados en pantalla al ejecutar esta opción:
• r.1.1: El porcentaje de vuelos cuya categoría de hotel coincide con la del primer vuelo que ingresó al vector.
Ejemplo de Salida:
r.1.1: 34
Opción 2: Mostrar todos los vuelos registrados, a razón de un Paquete por línea. Esta opción es de salida libre: no tiene
que respetar títulos especiales ni un formato específico.
Opción 3: Informar la cantidad de vuelos vendidos por cada combinación posible de aerolínea y categoría. Mostrar
únicamente los contadores mayores a cero, e indicando el nombre de la aerolínea y la descripción de la categoría. Al
momento de mostrar, primero deben aparecer todas las categorías con la primera aerolínea, luego todas las categorías
con la segunda, etc. etc.
Resultados esperados en pantalla al ejecutar esta opción:
• r.3.1.: El listado de combinaciones aerolínea / categoría junto a la cantidad de paquetes vendidos.
Ejemplo de salida:
r.3.1:
Fly Airways - Hostel: 40
Fly Airways - Resort: 3
AED te da alas - Económico: 15
Opción 4: Generar un archivo binario en el que se graben únicamente los vuelos que pertenezcan a la categoría c (valor
ingresado por teclado, sin requerimiento de validación), y tengan un precio superior al precio promedio general del
arreglo.
Resultados esperados en pantalla al ejecutar esta opción:
• r.4.1: El precio promedio de todos los elementos del arreglo.
• r.4.2: Precio acumulado de todos los paquetes guardados en el archivo.
Ejemplo de salida:
r.4.1.: 72344.55
r.4.2.: 68437577.98
Opción 5: En base al archivo generado en el punto 4, tome la cadena contenida en el campo observaciones del quinto
Paquete guardado en el archivo (si no hubiesen, al menos, 5 elementos en el archivo, procese la cadena “Categoría con
pocas ventas.”).
Resultados esperados en pantalla al ejecutar esta opción:
• r.5.1: La cantidad de palabras que contienen a las consonantes “d”, “n” o “r”, inmediatamente seguidas por una
vocal. El texto debe ser procesado obligatoriamente caracter a caracter, a razón de uno por vuelta de ciclo.
Ejemplo de salida:
r.5.1.: 7
Opción 0: Salir. El programa debe finalizar su ejecución. Agregue un mensaje libre para despedir al usuario.

"""
import R2class
from random import *
seed_set = False

def val(inf,message):
     n = int(input(message))
     while n < inf:
         n = int(input(message))
     return n

def generar_aleatorio():
    global seed_set
    if not seed_set:
        seed(1211)
        seed_set = True
    destinos = ["París", "Nueva York", "Tokio", "Londres", "Roma"]
    comentarios = [
    "¡Una experiencia inolvidable! Muy recomendado.",
    "Excelente servicio y comodidad.",
    "Muy recomendable para familias.",
    "Perfecto para una escapada romántica.",
    "Buena relación calidad precio."
        ]
    # Generación de cada variable necesaria
    codigo = ''.join(choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(5))
    destino = choice(destinos)
    aerolinea = randint(1, 5)
    categoria = randint(1, 6)
    precio = round(randint(100, 10000) + random(), 2)
    comentario = choice(comentarios)
    record = R2class.Paquete(codigo, destino, aerolinea, categoria, precio, comentario)
    return record

"""
Opción 3: Informar la cantidad de vuelos vendidos por cada combinación posible de aerolínea y categoría. Mostrar
únicamente los contadores mayores a cero, e indicando el nombre de la aerolínea y la descripción de la categoría. Al
momento de mostrar, primero deben aparecer todas las categorías con la primera aerolínea, luego todas las categorías
con la segunda, etc. etc.
Resultados esperados en pantalla al ejecutar esta opción:
• r.3.1.: El listado de combinaciones aerolínea / categoría junto a la cantidad de paquetes vendidos.
"""





def charge_order(v,record):
    right = len(v) -1
    left = 0
    pos = 0
    while left <= right:
        mid = (left + right)//2
        if record.precio == v[mid].precio:
            pos = mid
            break
        if record.precio < v[mid].precio:
            right = mid -1
        else:
            left = mid + 1

        if left > right:
            pos = left
    v[pos:pos] = [record]
    return v

def show(v):
    for record in v:
        print(record)



def main():
    v = []
    option = -1
    while option != 0:
        option = int(input("Ingrese opción: "))
        if option == 1:
            n = val(0,"porfavor ingrese un numero mayor 0: ")
            for i in range(n):
                record = generar_aleatorio()
                charge_order(v,record)

        elif option == 2:
            show(v)




if __name__ == "__main__":
    main()
    """
    Opción 1: Cargar en un arreglo n objetos del tipo Paquete, de tal forma que sus elementos se mantengan ordenados, en
todo momento, por precio de venta de forma ascendente (usar exclusivamente inserción ordenada con búsqueda
binaria, y genere en forma aleatoria los datos de cada objeto con la función generar_aleatorio() que se le ha provisto).
Cada vez que se ejecute esta opción, el vector debe iniciar vacío (en otras palabras, cada vez que se ejecute la opción, se
crea un nuevo vector vacío)
Resultados esperados en pantalla al ejecutar esta opción:
• r.1.1: El porcentaje de vuelos cuya categoría de hotel coincide con la del primer vuelo que ingresó al vector.

    :return:
    """