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
def average(acumulado,total):
    promedio = 0
    if total > 0:
        promedio = acumulado / total
    return promedio

def percentage(acumulado,total):
    porcentage = 0
    if total > 0:
        porcentage = acumulado * 100 / total
    return porcentage


def validate(inf,message):
    n = int(input(message))
    while n <= inf:
        n = int(input("porfavor, verifique que el numero sea menor a 0: "))
    return n

def charge(v,n):
    for i in range(n):
        name = carclass.name_gen()
        types = random.randint(0,3)
        brand = random.randint(1,15)
        quotes = random.randint(1,74)
        ammount = random.randint(150000,450000)
        record = carclass.Car(name,types,brand,quotes,ammount)
        add_order(v,record)

def add_order(v,record):
    left = 0
    right = len(v) -1
    pos = 0
    while left <= right:
        mid = (left + right)//2
        if v[mid].name == record.name:
            pos = mid
            break
        if record.name < v[mid].name:
            right = mid -1
        else:
            left = mid + 1
    if left > right:
        pos = left
    v[pos:pos] = [record]

def show(v):
    lines = carclass.header()
    for record in v:
        lines += str(record)
    print(lines)

def val_range(min,max,messi):
    n = min -1
    while n < min or n > max:
        n = int(input(messi))
        if n < min or n > max:
            print(f"porfavor, ingrese un valor entre{min} y {max}")
    return n

def search(v,nom):
    left = 0
    right = len(v) -1
    pos = -1
    while left <= right:
        mid = (right + left) //2
        if v[mid].name == nom:
            pos = mid
            break
        if nom < v[mid].name:
            right = mid -1
        else:
            left = mid + 1
    return pos
"""
5 - A partir de arreglo, genere un archivo binario con todas la ventas cuyo monto total facturado sea mayor a un valor num
 (num se ingresa desde teclado) y que el tipo de venta no sea 2. Muestre el archivo binario a razón de un registro por
 línea, al final del listado indique cual fue el monto promedio facturado para dichos clientes.
"""
def binary(v, file, num):
    m = open(file, "wb")
    for record in v:
        if record.ammount > num and record.types != 2:
            pickle.dump(record, m)
    m.close()

def read_binary(file):
    if not os.path.exists(file):
        print("No se ha cargado el archivo.")
        return

    m = open(file, "rb")
    size = os.path.getsize(file)
    lines = carclass.header()
    acumulador = contador = 0

    while m.tell() < size:
        record = pickle.load(m)
        lines += str(record)  # Muestra el registro en el listado
        acumulador += record.ammount  # Acumula el monto del auto
        contador += 1  # Cuenta el cliente

    m.close()

    # Llamada a la función average e integración al texto final
    promedio = average(acumulador, contador)
    lines += f"\nEl monto promedio facturado para estos clientes fue de: ${promedio:>10.2f}\n"

    print(lines)





def main():
    v = []
    print("1. Cargar vector")
    print("2. Mostrar vector")
    print("3. Buscar en vector")
    print("4. Generar binario y calcular")
    print("0. Cerrar archivo")
    option = -1
    while option !=0:
        option = val_range(0, 6, "porfavor ingrese un valor entre 0 y 6: ")
        if option == 1:
            n = validate(0, "porfavor, ingrese un numero mayor a 0: ")

            charge(v,n)
        elif option == 2:
            if len(v) >0:
                show(v)

        elif option == 3:
            if len(v) > 0:
             nom = input("ingrese el nombre y apellido: ")
             pos = search(v,nom)
             total = 0
             lines = carclass.header()
             if pos != -1:
                 print(f"cliente encontrado en:{v[pos]}")
                 x = val_range(1,74,"porfavor ingrese un numero de cuotas entre 1 y 74")
                 v[pos].quotes += x
                 lines += str(v[pos])
                 print(f"{lines}")
             else:
                 print("no encontrado")
        elif option == 4:
            if len(v) > 0:
                file = "facturas.dat"
                num = validate( 0, "Ingrese el monto mínimo facturado a filtrar: ")
                binary(v, file, num)
                read_binary(file)
            else:
                print("Por favor, primero cargue el vector.")

        else:
            print("porfavor, primero cargue el vector")


if __name__ == "__main__":
    main()
