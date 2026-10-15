"""
3. Concesionaria de Autos
Una concesionaria de autos solicita un programa para gestionar sus ventas. Por cada Venta se conoce el nombre del cliente
, el tipo de venta (un valor entre 0 y 3 incluido), marca de auto (un valor entre 1 y 15), la cantidad de cuotas pagas,
el monto total del plan. A través de un menú de opciones, realizar los siguientes puntos:

1 - Cargar un vector con n Ventas, creando todas las validaciones que considere necesarias, la carga puede ser manual,
 automática, o bien puede implementar ambas. El arreglo debe generarse de tal manera que el mismo siempre se encuentre
 ordenado por el nombre del cliente.
2 - Mostrar el contenido del arreglo a razón de un registro por línea.
3 - Buscar un cliente con el nombre nom (nom valor ingresado por parámetro). Si existe incrementar la cantidad de cuotas
en un valor x (donde x se lee desde teclado) y mostrar los datos. En caso de no existir indicar con un mensaje.
4 - A partir del arreglo, genere una matriz por cada tipo de venta y marca de auto, cada celda contendrá el monto acumulado
 total (un total de 60 contadores). Muestre de la matriz solo los valores mayores a cero.
5 - A partir de arreglo, genere un archivo binario con todas la ventas cuyo monto total facturado sea mayor a un valor num
 (num se ingresa desde teclado) y que el tipo de venta no sea 2. Muestre el archivo binario a razón de un registro por
 línea, al final del listado indique cual fue el monto promedio facturado para dichos clientes.
6 - A partir del arreglo, para un rango de marca de auto, donde los extremos del rango se ingresan por teclado,
determinar cual es la cantidad de cuotas pagas que se tienen y cual es el porcentaje que dichas cuotas representan sobre el total de cuotas pagas.
"""
import random
import carclass
import pickle
import os

def show(v):
    line_list = carclass.header()
    for registry in v:
        line_list += str(registry)
    print(line_list)

def validate(inf,message):
    n = int(input("cargue el vector con un numero mayor a 0: "))
    while n <= inf:
        n = int(input("error, cargue el vector con un numero mayor a 0"))
    return n

def add_order(v,registry):
    left = 0
    right = len(v) - 1
    pos = 0
    while left <= right:
        mid = (left + right) // 2
        if v[mid].name == registry.name:
            pos = mid
            break
        if registry.name < v[mid].name:
            right = mid-1
        else:
            left = mid + 1
    if left > right:
        pos = left
    v[pos:pos] = [registry]


def charge(n , v):

    for i in range(n):
        name = carclass.gen_name()
        types = random.randint(0,3)
        brand = random.randint(1,15)
        quote = random.randint(5,84)
        total = random.randint(3000000,45000000)
        registry = carclass.Carclass(name,types,brand,quote,total)
        add_order(v,registry)

"""
3 - Buscar un cliente con el nombre nom (nom valor ingresado por parámetro). Si existe incrementar la cantidad de cuotas
en un valor x (donde x se lee desde teclado) y mostrar los datos. En caso de no existir indicar con un mensaje.
"""
def search(v,nom):
    left = 0
    right = len(v) -1
    pos = -1
    while left <= right:
        mid = (left + right) //2
        if nom == v[mid].name:
            pos = mid
            break
        if nom < v[mid].name:
            right = mid - 1
        else:
            left = mid + 1
    return pos


def main():
    v = []
    option = -1
    print("1. cargar vector")
    print("2. mostrar vector")
    print("2. buscar nombre e incrementar cuota")
    print("0. cerrar programa")

    while option != 0:
        option = int(input("porfavor ,ingrese una opcion: "))
        if option == 1:
            n = validate(0,"ingrese un numero mayor a 0: ")
            charge(n,v)
        if option == 2:
            show(v)
        if option == 3:
            if len(v) >0:
                nom = input("ingrese el nombre: ")
                pos = search(v,nom)
                if pos != -1:
                    x = validate(0,"ingrese el numero de cuotas a aumentar: ")
                    v[pos].quote += x
                    print(carclass.header())
                    print(v[pos])
                else:
                    print(f"no existe '{nom}'")
            else:
                print("vector no cargado")





if __name__ == "__main__":
    main()
