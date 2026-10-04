"""
2. Empresa de TV+Internet
Una empresa proveedora de servicios de TV e Internet solicita un programa para gestionar su facturación. Por cada
cliente se define: identificación, nombre del titular, tipo de cliente (un valor entre 0 y 8 inclusive), tipo de producto
 (un valor en 0 y 15 inclusive), monto facturación mensual. A través de un menú de opciones, realizar los siguientes puntos:

1 - Cargar un vector de n facturas, validando todos los posibles valores, la carga puede ser manual, automática, o bien
 puede implementar ambas. El arreglo debe generarse de tal manera que el mismo siempre se encuentre ordenado por numero
 de identificación.

2 - Mostrar el contenido del vector a razón de un registro por línea.

3 - Buscar una factura con numero de identificación x, donde x se carga por teclado. Si existe mostrar sus datos, caso
contrario indicar con un mensaje.

4 - A partir del arreglo del punto 1, generar una matriz por tipo de cliente y tipo de producto, donde cada componente
contenga la cantidad de clientes  (144 contadores). Muestre de dicha matriz solo los valores que sean mayores a cero.

5 - A partir del arreglo, genere un archivo binario con todas las facturas que sean de un tipo x ingresado por parámetro
 y que su tipo de producto no sea ni 2, 3 o 4. Muestre los registros de ese archivo y al final indique cual fue el total
 facturado para todos esas facturas.

6 - A partir del arreglo, para un tipo de producto x que se ingresa por teclado informar cual fue el total facturado y
que porcentaje representa sobre el total de facturas del arreglo.

"""

"""
1 - Cargar un vector de n facturas, validando todos los posibles valores, la carga puede ser manual, automática, o bien
 puede implementar ambas. El arreglo debe generarse de tal manera que el mismo siempre se encuentre ordenado por numero
 de identificación.
"""

"""
Por cada
cliente se define: identificación, nombre del titular, tipo de cliente (un valor entre 0 y 8 inclusive), tipo de producto
 (un valor en 0 y 15 inclusive), monto facturación mensual.
"""
import random
import classnet
def validate(inf):
    n = int(input("porfavor, cargue el vector con un numero mayor a 0: "))
    while n <= inf:
        n = int(input("Error. porfavor, cargue el vector con un numero mayor a 0"))
    return n

def charge():
    n = validate(0)
    v = n * [None]
    names = ("lain", "fran", "zaira", "juliana", "melanie", "victoria,", "joaquin", "fer", "celeste", "fabricio",
             "freeman")

    for i in range(len(v)):
        ide = random.randint(1,20)
        name_choice = random.choice(names)
        type_client = random.randint(0,8)
        type_product = random.randint(0,15)
        total = random.randint(250000,1000000)
        v[i] = classnet.Netclass(ide,name_choice,type_client,type_product,total)
    return v

def show(v):
    n = len(v)
    for i in range(n-1):
        for j in range(i+1,n):
            if v[i].id > v[j].id:
                v[i],v[j] = v[j],v[i]

        print("el contenido del vector es", v[i])

"""
3 - Buscar una factura con numero de identificación x, donde x se carga por teclado. Si existe mostrar sus datos, caso
contrario indicar con un mensaje.

"""
def search(v):
    n = len(v)
    x = int(input("porfavor, cargue el numero de factura que busca: "))
    found = False
    for i in range(n):
        if v[i].id == x:
            print("la factura que busca es",v[i])
            found = True
            break
    if not found :
        print("no encontrado")

    return v

"""
4 - A partir del arreglo del punto 1, generar una matriz por tipo de cliente y tipo de producto, donde cada componente
contenga la cantidad de clientes  (144 contadores). Muestre de dicha matriz solo los valores que sean mayores a cero.
""" 
def count(v):
    n = len(v)
    matriz = 9 * [0]

    for i in range(9):
        matriz[i] = 16 *[0] #accedo a la matriz y cargo los contadores
    #contamos la acumulacion por cliente y producto
    for i in range(n):
        f = v[i].client_type
        c= v[i].product_type
        matriz[f][c] += 1



def main():
    v=[]
    option = -1
    while option != 5:
        print("porfavor, eliga una opcion:")
        print("1. Cargar vector")
        print("2. Mostrar vector")
        print("3. Mostrar factura")
        print("5. Cerrar vector ")
        option = int(input("porfavor, ingrese una opcion: "))
        if option == 1:
            v = charge()
        elif option ==2:
            if v:
                show(v)
            else:
                print("porfavor, cargue el vector")
        elif option == 3:
            if v:
                search(v)
            else:
                print("porfavor, cargue el vector")

        elif option == 5:
            print("programa finalizado")





if __name__ == "__main__":
    main()







