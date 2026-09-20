"""1. (Parcial 2019) - Servicios de Limpieza
Una compañía de servicios de limpieza desea un programa para procesar los datos de los trabajos ofrecidos.
Por cada trabajo se tienen los siguientes datos: el número de identificación del trabajo, la descripción o nombre del
mismo, el tipo de trabajo (un valor de 0 a 3, 0: interior, 1: exterior, 2: piletas, 3: tapizados), el importe a cobrar
por ese trabajo y la cantidad de personal afectado para prestar ese servicio. Se desea almacenar la
información referida a los n trabajos en un arreglo de registros de trabajos (definir el Trabajo y cargar n por teclado).

Se pide desarrollar un programa en Python controlado por un menú de opciones, que permita gestionar las siguientes tareas:
1- Cargar el arreglo pedido con los datos de los n trabajos. Valide que el número identificador del trabajo sea positivo
y que el importe a cobrar sea mayor a cero. Puede hacer la carga en forma manual, o puede generar los datos en forma automática
(con valores aleatorios) o puede disponer de ambas técnicas si lo desea. Pero al menos una debe programar.
2- Mostrar todos los datos de todos los trabajos, en un listado ordenado de mayor a menor según los importes a cobrar.
3- Determinar y mostrar los datos del trabajo que tenga la mayor cantidad de personal afectado (no importa si hay varios
trabajos con la misma cantidad máxima de personal: se pide mostrar uno y sólo uno cuya cantidad de personal sea máxima).
4- Determinar si existe un trabajo cuya descripción sea igual a d, siendo d un valor que se carga por teclado. Si existe,
 mostrar sus datos. Si no existe, informar con un mensaje. Si existe más de un registro que coincida con esos parámetros
 de búsqueda, debe mostrar sólo el primero que encuentre.
5- Determinar y mostrar la cantidad de trabajos por tipo."""
import class_19
import random

def validate(inf):
    number = int(input("input a number bigger than ",inf ))
    while number < inf:
        number = int(input("error. input a number bigger than ", inf))
    return number

"""
    def __init__(self,id_work,des,types,total,personal_quantity):
1- Cargar el arreglo pedido con los datos de los n trabajos. Valide que el número identificador del trabajo sea positivo
y que el importe a cobrar sea mayor a cero.
na compañía de servicios de limpieza desea un programa para procesar los datos de los trabajos ofrecidos.
Por cada trabajo se tienen los siguientes datos: 
el número de identificación del trabajo,
 la descripción o nombre del
mismo,
el tipo de trabajo (un valor de 0 a 3, 0: interior, 1: exterior, 2: piletas, 3: tapizados),
el importe a cobrar por ese trabajo y
la cantidad de personal afectado para prestar ese servicio.
Se desea almacenar la información referida a los n trabajos en un arreglo de registros de trabajos (definir el Trabajo y cargar n por teclado).

"""
def charge():
    number = validate(0)
    v = number * [None]
    descriptions = ("AUX", "PRIN", "PRO", "RES", "R", "U", "FONT")

    for i in range(number):
        id_work = random.randint(1,15000)
        des = (random.choice(descriptions))
        types = random.randint(0,3)
        total = random.randint(14000,30000)
        personal_quantity = random.randint(1,15)
        v[i] = class_19.Service(id_work,des,types,total,personal_quantity) #number viene de la funcion validate
    return v

"""
2- Mostrar todos los datos de todos los trabajos, en un listado ordenado de mayor a menor según los importes a cobrar.

"""
def search(v):
    number = len(v)
    for i in range (number -1):
        for j in range(i+1 , number):
            if v[i].total < v[j].total:
                v[i], v[j] = v[j],v[i]

    print("los listados ordenados de mayor a menor son:")
    for k in range(number):
        print(v[k])

"""
3- Determinar y mostrar los datos del trabajo que tenga la mayor cantidad de personal afectado (no importa si hay varios
trabajos con la misma cantidad máxima de personal: se pide mostrar uno y sólo uno cuya cantidad de personal sea máxima).
"""

def count(v):
    number = len(v)
    max = v[0]
    for i in range(number):
        if v[i].personal_quantity > max.peronal_quantity:
            max = v[i]
    print("lain says: ", v[i])

def principal(v):
    option = -1
    while option != 5:
        if option == 1:
            charge()


if __name__ == "__main__":
    principal()