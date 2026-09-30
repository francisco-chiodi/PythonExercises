"""
Una agencia de empleos necesita un programa para procesar los datos de los empleos que ofrece a los
interesados. Por cada Empleo se tienen los siguientes datos: el número de identificación del empleo, la descripción
del empleo, el tipo de empleo (un valor del 0 al 39) y el monto mensual del sueldo o retribución que se paga por
ese empleo. Se desea almacenar la información referida a los n empleos en un arreglo de objetos de tipo Empleo
(definir la clase Empleo y cargar n por teclado, validando que sea mayor a cero). Se pide desarrollar un programa
en Python controlado por un menú de opciones, que permita gestionar las siguientes tareas:
1. Cargar el arreglo pedido con los datos de los n empleos. Valide o asegure que los valores de cada campo sean
correctos. Puede hacer la carga en forma manual, o puede generar los datos en forma automática (con valores
aleatorios). Pero al menos una debe programar. Pero si hace carga automática, todos los campos deben ser
cargados así (no combine ambas técnicas en la carga de un registro).
2. Mostrar todos los datos de todos los empleos, a razón de uno por línea, en un listado ordenado de menor a
mayor según la descripción de los empleos. Al final del listado indique la suma de los sueldos a pagar por todos
los empleos que se mostraron.
3. Determinar la cantidad de empleos que hay en el arreglo por cada tipo de empleo posible (40 contadores en
total en un vector de conteo). Muestre solo los valores de los contadores cuyos valores finales sean mayores a
cero.
4. Determinar si existe un empleo cuyo número de identificación sea igual num, siendo num un valor que se carga
por teclado. Si existe, mostrar solo su descripción y el sueldo a pagar. Si no existe, informar con un mensaje. Si
existe más de un registro que coincida con esos parámetros de búsqueda, debe mostrar sólo el primero que
encuentre. La búsqueda debe detenerse al encontrar el prime objeto que coincida con el criterio pedido
"""
import classT1
import random


def charge(v):
    n = int(input("ingrese la cantidad de elementos del arreglo"))
    v = n * [None]
    description = ("mecanico","ingeniero","programador","arquitecto","abanil","agrimensor","disenador","piletero","abogado")
    for i in range(n):
        id = random.randint(100,1500)
        des = random.choice(description)
        types = random.randint(0,39)
        total = random.randint(10000,50000)
        v[i] = classT1.Empleo(id,des,types,total)
    return v

"""
2. Mostrar todos los datos de todos los empleos, a razón de uno por línea, en un listado ordenado de menor a
mayor según la descripción de los empleos. Al final del listado indique la suma de los sueldos a pagar por todos
los empleos que se mostraron.
"""

def show(v):
    n = len(v)
    total = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if v[i].des > v[j].des:
                v[i], v[j] = v[j],v[i]

    for i in range(n):
        print(v[i])
        total += v[i].total

    print("la suma del total de los sueldos es ", total)





def principal():
    v = []
    option = -1
    while option !=5:
        print("opcion 1: cargar vector")
        print("opcion 2: mostrar vector")
        print("opcion 5: cerrar vector")

        option  = int(input("ingrese una opcion "))
        if option == 1:
            v = charge(v)
        if option == 2:
            show(v)

if __name__ == "__main__":
    principal()

