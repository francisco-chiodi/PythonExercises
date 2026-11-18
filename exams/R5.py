"""
Una fábrica que vende paquetes de galletas surtidas necesita un programa para gestionar sus productos. Por cada
producto se conoce: el código de producto (un número entero), el tipo de presentación (un entero entre 1 y 10; Ej:
1→Bolsa 400gr, 2→Caja 700gr, etc.), una frase que se incluye al frente del paquete (una cadena terminada en "." con
palabras separadas por un blanco, por ejemplo: "Pruebe nuestras galletas y a-pruebe AED."), la cantidad de sellos de
etiquetado frontal (un entero entre 0 y 4) y el precio sugerido. Se pide:
1. Cargar un arreglo con los datos de n objetos de la clase Producto de manera que en todo momento se
mantenga ordenado por código de producto. Para esto debe utilizar el algoritmo de inserción
ordenada con búsqueda binaria (se considerará directamente incorrecta la solución basada en cargar
el arreglo completo y ordenarlo al final, o aplicar el algoritmo de inserción ordenada pero con
búsqueda secuencial). Valide la carga del valor n. Debe generar los datos en forma automática (con
valores aleatorios).
2. Mostrar todos los objetos a razón de uno por línea, indicando al final del listado el porcentaje que
representan respecto al total los productos que tienen 0 sellos.
3. Calcular y mostrar la cantidad de productos que se venden por cada combinación posible de tipo de
presentación y cantidad de sellos. Esto es: una matriz de conteo con 10*5 contadores). Mostrar
únicamente las combinaciones con valor mayor a cero.
4. A partir del arreglo creado en el punto 1, genere un archivo binario que contenga todos los objetos
cuyo precio sugerido esté entre los valores p1 y p2 (valores cargados por teclado, sin el requerimiento
de validar la carga).
5. Muestre el archivo creado en el punto anterior y al final muestre una línea adicional indicando la
cantidad de registros que se mostraron.
6. Tome la cadena contenida en el campo frase del último objeto del vector, e informe la cantidad de
palabras de esa cadena que comiencen con una vocal (mayúscula o minúscula) y que además tengan
en cualquier lugar una "s" o una "m". El texto debe ser procesado obligatoriamente caracter a
caracter, a razón de uno por vuelta de ciclo.
"""
import R5class
import random
import pickle
import os

def percentage(quantity,total):
    return (quantity * 100)//total

def val(inf,message):
    n = int(input(message))
    while n <= inf:
        n = int(input(message))
    return n


def gen(v):
    n = val(0, "porfavor ingrese un numero mayor a 0: ")

    for i in range(n):
        codigo = random.randint(100,2000)
        tipo = random.randint(1,10)
        frase = (
            "Pruebe nuestras galletas y a-pruebe AED.",
            "Sabor artesanal con ingredientes seleccionados.",
            "Ideal para compartir en cada merienda.",
            "Nueva receta crocante sin conservantes.",
            "Calidad y frescura en cada bocado.",
            "Descubra el autentico sabor casero.",
            "Edicion especial para fanaticos del dulce.",
            "Textura suave y aroma irresistible.",
            "El acompanante perfecto para su cafe.",
            "Hecho con pasion y tradicion familiar."
            )
        frases = random.choice(frase)
        sellos = random.randint(0,4)
        precio = random.randint(1000,10000)
        record = R5class.Productos(codigo,tipo,frases,sellos,precio)
        order(v,record)


def order(v, record):
    left = 0
    right = len(v) -1
    pos = 0
    while left <= right:
        mid = (left + right)//2
        if record.codigo == v[mid].codigo:
            pos = mid
            break

        if record.codigo > v[mid].codigo:
            right = mid - 1
        else:
            left = mid + 1

        if left > right:
            pos = left

    v[pos:pos] = [record]

""""
2. Mostrar todos los objetos a razón de uno por línea, indicando al final del listado el porcentaje que
representan respecto al total los productos que tienen 0 sellos.
"""
def show(v):
    quantity = 0
    total = 0
    for record in v:
        print(record)
        quantity += 1
        if record.sellos == 0:
            total += 1
    por = percentage(quantity,total)
    print("el porcentaje de los productos que tienen 0 sellos es: ", por)






def menu():
    print("=== MENU PRINCIPAL ===")
    print("1. Cargar vector")
    print("2. Mostrar vector")


def main():
    v = []
    menu()
    option = -1
    while option != 0:
        option = int(input("porfavor ingrese una opcion: "))

        if option == 1:
             gen(v)


        if option == 2:
            show(v)

if __name__ == "__main__":
    main()