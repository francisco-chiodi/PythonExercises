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
import netclass
import pickle
import os
def validate(inf,message):
    n = int(input(message))
    while n <= inf:
        n = int(input("error, porfavor que sea mayor a 0: "))
    return n

def add_order(v,record):
    left = pos = 0
    right = len(v) -1
    while left <= right:
        mid = (left + right) // 2
        if v[mid].iden == record.iden:
            pos = mid
            break
        if record.iden < v[mid].iden:
            right = mid -1
        else:
            left = mid + 1
    if left > right:
        pos = left
    v[pos:pos] = [record]

def show(v):
    lines = netclass.header()
    for record in v:
        lines += str(record)
    print(lines)

def charge(v,n):
    for record in range(n):
        iden = random.randint(1,1000)
        name = netclass.gen_name()
        type_client = random.randint(0,8)
        type_product = random.randint(0,15)
        ammount = random.uniform(15000,50000)
        record = netclass.Net(iden,name,type_client,type_product,ammount)
        add_order(v,record)

"""
3 - Buscar una factura con numero de identificación x, donde x se carga por teclado. Si existe mostrar sus datos,
 caso contrario indicar con un mensaje.
"""

def search(v,ids):
    left = 0
    right = len(v) - 1
    pos = -1
    while left <= right:
        mid = (left + right) // 2
        if v[mid].iden == ids:
            pos = mid
            break
        if ids < v[mid].iden:
            right = mid - 1
        else:
            left = mid + 1
    return pos

def average(acumulado,cantidad):
    promedio = 0
    if cantidad > 0:
        promedio = acumulado/cantidad
    return promedio

def porcentage(acumulado,total):
    porcentaje = 0
    if acumulado > 0:
        porcentaje = acumulado * 100 / total
    return porcentaje

def make_binari(v,facturas,num):
    m = open(facturas,"wb")
    for record in v:
        if record.type_client == num and record.type_product not in (2,3,4):
            pickle.dump(record,m)
    m.close()

def show_binari(facturas):
    if not os.path.exists(facturas):
        print(f"archivo no cargado")
        return
    m = open(facturas, "rb")
    size = os.path.getsize(facturas)
    lista = netclass.header()
    total_facturado = 0
    while m.tell() < size:
        record = pickle.load(m)
        lista += str(record)
        total_facturado += record.ammount
    m.close()
    lista += f"el total facturado mensual fue de {total_facturado:>10.2f}"
    print(lista)

def range_val(min, max, message):
    n = min - 1
    while n < min or n > max:
        n = int(input(message))
        if n < min or n > max:
            print(f"Error, debe ingresar un valor entre {min} y {max}")
    return n



"""
 5 - A partir del arreglo, genere un archivo binario con todas las facturas que sean de un tipo x ingresado por parámetro
                   y que su tipo de producto no sea ni 2, 3 o 4. Muestre los registros de ese archivo y al final indique cual fue el total
                    facturado para todos esas facturas.
"""


def main():
    v = []
    print("1. Cargar vector")
    print("2. Mostrar vector")
    print("3. Buscar identificacion")
    print("0. Cerrar vector")
    option = -1
    while option != 0:
        option = int(input("porfavor, ingrese una opcion: "))
        if option == 1:
            n = validate(0,"cargue el vector con un numero mayor a 0: ")
            charge(v,n)
            print("vector cargado exitosamente")
        if option == 2:
            if len(v) > 0:
                show(v)
            else:
                print("porfavor, primero cargue el vector")

        elif option == 3:
            if len(v) > 0:
                ids = int(input("indique el id buscado: "))
                pos = search(v,ids)
                if pos != -1:
                    lines = netclass.header()
                    print(f"se encontro la coincidencia{v[pos]}")
                else:
                    print("no se encontro ninguna coincidencia")

        elif option == 5:
            if len(v) > 0:
                num = range_val(0,8,"ingrese el cliente a filtrar (0 a 8")
                facturas = "facturas.dat"
                make_binari(v,facturas,num)
                show_binari(facturas)
            else:
                print("porfavor , cargue antes el vector")





            """
            5 - A partir del arreglo, genere un archivo binario con todas las facturas que sean de un tipo x ingresado por parámetro
             y que su tipo de producto no sea ni 2, 3 o 4. Muestre los registros de ese archivo y al final indique cual fue el total
              facturado para todos esas facturas.
            """
if __name__ == "__main__":
    main()