
"""
Una empresa de seguridad desea un programa para gestionar los servicios de monitoreo de alarmas de sus
clientes. Por cada Servicio de alarma vendido a un cliente se tiene
un código identificatorio (un número entero),
el nombre del cliente (una cadena),
un valor entre 1 y 10 que indica el tipo de servicio prestado,
 y el importe a pagar por mes por ese servicio.
Se desea almacenar la información de n servicios de alarma en un arreglo de objetos (la
cantidad n se debe cargar por teclado). Se pide desarrollar un programa en Python controlado por un menú de
opciones y que posea como mínimo dos módulos, que permita gestionar las siguientes tareas:
a. Cargar el arreglo pedido con los datos de los n servicios. Debe validar o asegurar que los datos sean siempre
correctos. Si hace carga automática
b. Mostrar los datos de todos los servicios cuyo importe esté entre los valores i1 e i2 (ambos incluidos) que se
cargan por teclado, y ordenados de menor a mayor por código identificatario. Muestre al final una línea
adicional con la cantidad de servicios mostrados en este listado.
c. Determinar cuántos servicios hay para uno de los tipos posibles (10 contadores). Mostrar todos los conteos
que sean diferentes de cero.
d. Determinar si existe un servicio cuyo nombre de cliente sea igual a nom (cargar nom por teclado). Si lo
encuentra, cambie el valor del atributo importe, sumando 2000 al valor anterior, y muestre todos los datos de
ese objeto modificado. Si no lo encuentra, informe con un mensaje que no existe. Debe detener la búsqueda
en el primero que encuentre (sin importar si hay más de un objeto que cumpla el criterio pedido).

"""

import random
import clase_3

def validate(inf):
    number = int(input("ingrese el numero: "))
    while number <= inf:
        print("error, se le pidio mayor a ",str(inf), "ingrese nuevamente el numero:")
        number = int(input("ingrese el numero: "))
    return number

"""
a. Cargar el arreglo pedido con los datos de los n servicios. Debe validar o asegurar que los datos sean siempre
correctos:
un código identificatorio (un número entero),
el nombre del cliente (una cadena),
un valor entre 1 y 10 que indica el tipo de servicio prestado,
 y el importe a pagar por mes por ese servicio.
"""
def charge():
    number = validate(0)
    v = number * [None]
    names = ("kira", "fran", "lain", "juli", "lain ikawura", "oro", "anahi", "selene", "freeman")
    apellidos = ("Díaz", "Giuliani", "Trejo", "Masiero", "Duplesis", "Johnson", "Iriarte")
    for i in range(number):
        client_name = random.choice(names) + random.choice(apellidos) + str(i)
        id_code = random.randint(1,1000)
        service_type = random.randint(1,10)
        total = round(random.uniform(300,1500),2)
        v[i] = clase_3.Services(client_name,id_code,service_type,total)
        print("arreglo generaddo")
        print()
    return v
"""
Mostrar los datos de todos los servicios cuyo importe esté entre los valores i1 e i2 (ambos incluidos) que se
cargan por teclado, y ordenados de menor a mayor por código identificatario. Muestre al final una línea
adicional con la cantidad de servicios mostrados en este listado.
"""

def show(v):
    number = len(v)
    for i in range(number-1):
        for j in range(i+1 , number):
            if v[i].id_code > v[j].id_code:
                v[i],v[j] = v[j],v[i]
    cs = 0
    i1 = int(input("ingrese el valor inferior del importe"))
    i2 = int(input("ingrese el valor superior del importe"))
    print("Listado de servicios con importe entre", i1, "y", i2, ":" )
    for i in range(number):
       if i1 <= v[i].total <= i2:
           cs += 1
           print(v[i])
    print("cantidad de servicios mostrados: ", cs)

"""
c. Determinar cuántos servicios hay para uno de los tipos posibles (10 contadores). Mostrar todos los conteos
que sean diferentes de cero. es lo mismo que decir  "Determinar cuántos servicios fueron contratados por cada tipo 
de producto vendido (mostrando solo los tipos que registraron ventas)."
"""

def count(v):
    number = len(v) #cantidad de clientes que contratan tipos de servicios
    counter_service = 10 *[0] #10 servicios fijos
    for i in range(number):
        indice = v[i].service_type - 1  #restamos uno para compatibilizar con los indices del vector.
        counter_service[indice] += 1
    print("cantidad de servicios por tipo: ")
    for k in range(10):
        if counter_service[k] > 0:
            # si al contar/acumular resté uno, entonces en pantalla, y SOLO EN PANTALLA, mostrar k+1...
            print("Tipo de servicio:", k + 1, "Cantidad:", counter_service[k])
    print()

"""
. Determinar si existe un servicio cuyo nombre de cliente sea igual a nom (cargar nom por teclado). Si lo
encuentra, cambie el valor del atributo importe, sumando 2000 al valor anterior, y muestre todos los datos de
ese objeto modificado. Si no lo encuentra, informe con un mensaje que no existe. Debe detener la búsqueda
en el primero que encuentre (sin importar si hay más de un objeto que cumpla el criterio pedido).
"""

def search(v):
    n = len(v)
    nom = input("Nombre del cliente a buscar: ")
    for i in range(n):
        if nom == v[i].nombre:
            print("Encontrado - Datos actuales:")
            print(v[i])
            v[i].importe += 2000
            print("Datos con el importe actualizado:")
            print(v[i])
            print()
            return
    print("No estaba...")
    print()



def principal():
    v = []
    op = -1
    while op != 5:
        print("1. Cargar arreglo")
        print("2. Mostrar ordenado")
        print("3. Contar por tipo")
        print("4. Buscar")
        print("5. Salir")
        op = int(input("Ingrese número de opción: "))

        if op == 1:
            v = cargar()

        elif op == 2:
            if v:
                mostrar(v)
            else:
                print("el vector no fue cargado todavía...")
                print()

        elif op == 3:
            if v:
                contar(v)
            else:
                print("el vector no fue cargado todavía...")
                print()

        elif op == 4:
            if v:
                buscar(v)
            else:
                print("el vector no fue cargado todavía...")
                print()

        elif op == 5:
            print("Programa terminado... Hasta la vista baby...")
            print()


if __name__ == "__main__":
    principal()
