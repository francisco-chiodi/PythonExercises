"""
Una empresa proveedora de servicios de TV e Internet solicita un programa para gestionar su facturación.
 Por cada cliente se define: identificación, nombre del titular, tipo de cliente (un valor entre 0 y 8 inclusive),
 tipo de producto (un valor en 0 y 15 inclusive), monto facturación mensual. A través de un menú de opciones, realizar
 los siguientes puntos:

1 - Cargar un vector de n facturas, validando todos los posibles valores, la carga puede ser manual, automática,
o bien puede implementar ambas. El arreglo debe generarse de tal manera que el mismo siempre se encuentre ordenado
por numero de identificación.

2 - Mostrar el contenido del vector a razón de un registro por línea.

3 - Buscar una factura con numero de identificación x, donde x se carga por teclado. Si existe mostrar sus datos,
 caso contrario indicar con un mensaje.

4 - A partir del arreglo del punto 1, generar una matriz por tipo de cliente y tipo de producto, donde cada componente
 contenga la cantidad de clientes  (144 contadores). Muestre de dicha matriz solo los valores que sean mayores a cero.

5 - A partir del arreglo, genere un archivo binario con todas las facturas que sean de un tipo x ingresado por parámetro
 y que su tipo de producto no sea ni 2, 3 o 4. Muestre los registros de ese archivo y al final indique cual fue el total
  facturado para todos esas facturas.

6 - A partir del arreglo, para un tipo de producto x que se ingresa por teclado informar cual fue el total facturado
y que porcentaje representa sobre el total de facturas del arreglo.
"""
import random
import interclass
import pickle
import os

def validate(inf,message):
    n = int(input(message))
    while n <= inf:
        n = int(input("porfavor, que sea mayor a 0: "))
    return n

def charge(v,n):

    for i in range(n):
        ide = random.randint(1,1000)
        name = interclass.name_gen()
        type_client = random.randint(0,8)
        type_product = random.randint(0,15)
        ammount = random.randint(10000,40000)
        record = interclass.Inter(ide,name,type_client,type_product,ammount)
        add_order(v,record)

def add_order(v,record):
    left = pos =0
    right = len(v) -1
    while left <= right:
        mid = (left + right)//2
        if v[mid].ide == record.ide:
            pos = mid
            break
        if record.ide < v[mid].ide:
            right = mid -1
        else:
            left = mid + 1
    if left > right:
        pos = left
    v[pos:pos] = [record]

def val_range(min,max,message):
    n = min -1
    while n < min or n > max:
        n = int(input(message))
        if n < min or n > max:
            print(f"porfavor, que sea entre {min} y {max}")
    return n

def show(v):
    lines = interclass.header()
    for record in v:
        lines += str(record)
    print(lines)


def search(v,x):
    left = 0
    right = len(v) -1
    pos = -1
    while left <= right:
        mid = (left + right)//2
        if v[mid].ide == x:
            pos = mid
            break
        if x < v[mid].ide:
            right = mid - 1
        else:
            left = mid + 1
    return pos



def binary(v,file,x):
    m = open(file, "wb")
    print("porfavor, busque clientes con numeros que no sean 2,3 y 4")
    for record in v:
        if record.type_client == x and record.type_product not in (2,3,4):
            pickle.dump(record,m)
        else:
            print("porfavor, reinicie la busqueda")
    m.close()
def binary_read(file):
    if not os.path.exists(file):
        print(f"no se ha cargado el archivo {file} ")
        return
    m = open(file,"rb")
    size = os.path.getsize(file)
    lines = interclass.header()
    total = 0
    while m.tell() < size:
        record = pickle.load(m)
        lines += str(record)
        total += record.ammount

    m.close()
    lines += f" el toal calculado fue {total}"
    print(f"{lines}")

def main():
    v = []
    print("1. Cargar vector")
    print("2. Mostrar vector ordenado")
    print("3. Buscar y mostrar id")
    print("4. Generar archivo binario" )
    print("0. Cerrar programa")
    option =-1
    while option != 0:
        option = val_range(0,6,"porfavor, ingrese una opcion entre 0 y 6: ")
        if option == 1:
            n = validate(0, "porfavor, ingrese un numero mayor a 0: ")
            charge(v,n)
            print("vector cargado con exito")
        elif option == 2:
            if len(v) > 0:
                show(v)
            else:
                print("porfavor antes cargue el vector")
        elif option == 3:
            if len(v) > 0:
                x = val_range(1,1000,"porfavor, ingrese un numero de id entre 1 y 1000: ")
                pos = search(v,x)
                if pos != -1:
                    lines = interclass.header()
                    lines += str(v[pos])
                    print(f"se encontro una coincidencia: {lines} ")
                else:
                    print(f"no se encontro ninguna coincidencia.")
            else:
                print("porfavor, primero cargue el vector")

        elif option == 4:
            if len(v) > 0:
                x = val_range(0,8,"ingrese clientes entre 0 y 8")
                file = "facturas.dat"
                binary(v,file,x)
                binary_read(file)
            else:
                print("no se ha cargado el vector")



"""

A partir del arreglo, genere un archivo binario con todas las facturas que sean de un tipo x ingresado por parámetro
 y que su tipo de producto no sea ni 2, 3 o 4. Muestre los registros de ese archivo y al final indique cual fue el total
  facturado para todos esas facturas.
"""


if __name__ == "__main__":
    main()
