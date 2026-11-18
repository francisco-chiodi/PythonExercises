import R3class
from random import *
seed_set = False
import pickle
import os

def generar_aleatorio():
    global seed_set
    if not seed_set:
        seed(1211)
        seed_set = True
    titulos = ["El Gran Escape", "La Aventura Infinita",
    "Misterio en la Noche", "El Secreto del Bosque",
    "Viaje al Centro de la Tierra"]
    opciones_sinopsis = ["Una emocionante aventura llena de giros inesperados.",
    "Una historia de amor y valentía en tiempos difíciles.",
    "Un thriller que te mantendrá al borde de tu asiento.",
    "Una comedia que te hará reír a carcajadas.",
    "Un drama conmovedor sobre la vida y la esperanza."]
    codigo = randint(1000, 10000)
    titulo = choice(titulos)
    sala = randint(1, 12)
    puntuacion = randint(1, 10)
    sinopsis = choice(opciones_sinopsis)
    record = R3class.Pelicula(codigo,titulo,sala,puntuacion,sinopsis)
    return record

def val(inf,message):
    n = int(input(message))
    while n < inf:
        n = int(input(message))
    return n


def menu():
    print("=== Menu de opciones ===")
    print("1. Cargar arreglo con n objetos.")
    print("2. Mostrar todas las pelicuas registradas.")
    print("3. Generar binario.")
    print("4. Buscar codigo mas bajo.")

"""
por título de forma descendente 
"""
def show(v):
    counter = 0
    for record in v:
        counter += 1
        print(record)

def charge_order(v,record):
    left = 0
    right = len(v) -1
    pos = 0
    while left <= right:
        mid = (left + right)//2
        if record.titulo == v[mid].titulo:
            pos = mid
            break
        if record.titulo > v[mid].titulo:
            left = mid + 1
        else:
            right = mid -1

        if left > right:
            pos = left
    v[pos:pos] = [record]
    return v

"""
Opción 3: Generar un archivo binario con las películas cuya sala sea igual a s (valor ingresado por teclado, sin exigencia
de validación) y con puntuación mayor a 6.

"""
def gen_bin(v,archive,s):
    m = open(archive,"wb")
    for record in v:
        if record.sala == s and record.puntuacion > 6:
            pickle.dump(record,m)
    m.close()

"""
Opción 4: Utilizando el archivo generado en el punto 3, informar cuál es el título de la película con el código más bajo.
"""
def read_bin(archive):
    if not os.path.exists(archive):
        print("El archivo no existe.")
        return None

    size = os.path.getsize(archive)
    if size == 0:
        print("El archivo está vacío.")
        return None

    menor = None
    m = open(archive, "rb")
    while m.tell() < size:
        record = pickle.load(m)
        if menor is None or record.codigo < menor.codigo:
            menor = record
    m.close()

    return menor.titulo

"""
Opción 5: Buscar en el vector si existe una película cuyo código sea igual a un valor cod ingresado por teclado. Si se
encuentra, utilizar la sinópsis de la misma para entregar el resultado r.5.1, que se describe más adelante. Si no se
encuentra la película, utilizar la cadena “La película no fue agregada al catálogo del festival, lo sentimos.”.
"""
"""

"""

def search(v,cod):
    for record in v:
        if record.codigo == cod:
            print("la sinopsis es: ", record.sinopsis)
            word = record.sinopsis
            return word
    return print("la pelocula no fue agregada al catálogo del festival, lo sentimos.")

"""
r.5.1: La cantidad de palabras que contienen a las consonantes “d”, “n” o “r”, inmediatamente seguidas por una
vocal. El texto debe ser procesado obligatoriamente caracter a caracter, a razón de uno por vuelta de ciclo.
Ejemplo de salida:
"""
def es_vocal(letra):
    return letra.lower() in "aeiouáéíóúü"


def procesar_sinopsis(sinopsis):
    cantidad_palabras = 0
    tiene_par = False
    anterior = ""

    for letra in sinopsis:
        if letra != " " and letra != ".":
            # Si la letra anterior fue d/n/r Y la actual es vocal, marcamos la palabra
            if anterior.lower() in "dnr" and es_vocal(letra):
                tiene_par = True
            # Guardamos la letra actual como 'anterior' para la próxima vuelta
            anterior = letra
        else:
            # Fin de palabra: si cumplió en algún momento, sumamos 1 palabra
            if tiene_par:
                cantidad_palabras += 1
            # Reiniciamos para la palabra siguiente
            tiene_par = False
            anterior = ""

    print(f"r.5.1.: {cantidad_palabras}")

def main():
    v = []
    menu()
    option = -1
    while option != 0:
        option = int(input("ingrese opcion: "))
        if option == 1:
            n = val(0,"ingrese un numero mayor a 0: ")
            for i in range(n):
                record = generar_aleatorio()
                charge_order(v, record)

        if option == 2:
            show(v)

        if option == 3:
            s = int(input("ingrese el numero de sala: "))
            archive = "archive.dat"
            gen_bin(v,archive,s)

        if option == 4:
            titulo = read_bin(archive)
            print("el tamano del codigo mas chico es: ",titulo)

        if option == 5:
            cod = int(input("ingrese el codigo de la pelicula: "))
            search(v,cod)
            word = search(v,cod)
            vocal(word)





if __name__ == "__main__":
    main()