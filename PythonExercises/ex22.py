"""2. (Parcial 2021) - Empresa Agropecuaria
Se pide desarrollar un programa en Python para el enunciado que sigue. El programa obligatoriamente deberá plantearse
 como un proyecto que contenga al menos dos módulos (uno para la definición del tipo de registro y las funciones para
  gestionarlo (a criterio del estudiante) y otro módulo deberá contener el programa principal que obligatoriamente debe
   ser planteado en base a un menú de opciones y con funciones para toda situación posible.

Una empresa agropecuaria necesita un programa para procesar los datos de los trabajos ofrecidos. Por cada trabajo
 se tienen los siguientes datos:
 el número de identificación,
 la descripción del trabajo,
el tipo de trabajo (un número
entero entre 0 y 19, para indicar por ejemplo: 0: siembra, 1: control de plagas, 2: cosecha, etc.)
el importe acobrar por ese trabajo
la cantidad de personal afectado al mismo.

Se desea almacenar la información referida aestos trabajos en un arreglo de registros de tipo Trabajo (definir el tipo
Trabajo y cargar n por teclado).

Se pide desarrollar un programa en Python controlado por un menú de opciones y que posea como mínimo dos módulos, que
permita gestionar las siguientes tareas:

1-      Cargar el arreglo pedido con los datos de los n trabajos. Valide que el número identificador del trabajo sea
positivo y que el tipo del servicio esté entre 0 y 19. Puede hacer la carga en forma manual, o puede generar los datos
 en forma automática (con valores aleatorios) o puede disponer de ambas técnicas si lo desea. Pero al menos una debe
 programar.

2-      Mostrar todos los datos de todos los trabajos cuya cantidad de personal sea mayor a 3, en un listado ordenado
 de mayor a menor según los números de identificación de esos trabajos. Al final del listado, mostrar además la suma de
  los importes de todos los registros mostrados.

3-      Determinar y mostrar la cantidad de trabajos que se ofrecen de cada tipo posible de (un contador para los
trabajos tipo 0, otro para el tipo 1, etc.) En total, 20 contadores. Muestre solo los resultados mayores a cero.

4-      Mostrar los datos de todos los trabajos cuyo importe a cobrar sea mayor al importe promedio de todos los
 trabajos del arreglo

5-      Determinar si existe un trabajo cuyo número de identificación sea igual a num y que sea del tipo t, siendo
num y t dos valores que se cargan por teclado. Si existe, mostrar sus datos. Si no existe, informar con un mensaje.
Si existe más de un registro que coincida con esos parámetros de búsqueda, debe mostrar sólo el primero que encuentre."""
import class_22
import random
def validate(inf):
    number = int(input("ingrese un numero mayor a 0" ))
    while number <= inf:
        number = int(input("error, ingrese un numero valor a 0"))
    return number

"""
1-      Cargar el arreglo pedido con los datos de los n trabajos. Valide que el número identificador del trabajo sea
positivo y que el tipo del servicio esté entre 0 y 19. Puede hacer la carga en forma manual, o puede generar los datos
 en forma automática (con valores aleatorios) o puede disponer de ambas técnicas si lo desea. Pero al menos una debe
 programar.
  se tienen los siguientes datos:
 el número de identificación,
 la descripción del trabajo,
el tipo de trabajo (un número
entero entre 0 y 19, para indicar por ejemplo: 0: siembra, 1: control de plagas, 2: cosecha, etc.)
el importe acobrar por ese trabajo
la cantidad de personal afectado al mismo.
    def __init__(self,id_num,des,types,total,personal_quantity):

"""
def charge():
    number = validate(0)
    v = number * [None]
    description = ("AB","PRO","AUX","INS","FOX","FR","ST")
    for i in range(number):
        id_num = random.randint(1,20000)
        des = random.choice(description)
        types = random.randint(0,19)
        total = round(random.randint(15000,60000),2)
        personal = random.randint(1,15)
        v[i] = class_22.Trabajo(id_num,des,types,total,personal)
    return v

"""
2-      Mostrar todos los datos de todos los trabajos cuya cantidad de personal sea mayor a 3, en un listado ordenado
 de mayor a menor según los números de identificación de esos trabajos. Al final del listado, mostrar además la suma de
  los importes de todos los registros mostrados.
"""

def show(v):
    number = len(v)
    add = 0
    for i in range (number-1):
        for j in range(i+1,number):
            if v[i].id_num < v[j].id_num:
                v[i],v[j] = v[j],v[i]
    print("los datos ded los trabajos cuya cantiad de personal son mayor a 3 son: ")
    for k in range(number):
        if v[k].personal_quantity > 3:
            print(v[k])
            add += v[k].total

    print("la suma de todos lo registros es", add)


"""
3-      Determinar y mostrar la cantidad de trabajos que se ofrecen de cada tipo posible de (un contador para los
trabajos tipo 0, otro para el tipo 1, etc.) En total, 20 contadores. Muestre solo los resultados mayores a cero.
"""

def count(v):
    number = len(v)
    counter = 20 * [0]
    for i in range(number):
        index = v[i].types
        counter[index] += 1
    print("Cantidad de trabajos ofrecidos por tipo (solo mostrando con más de 0 trabajos):")
    for k in range(20):
        if counter[k] > 0:
            print("Para el tipo de trabajo", k, "la cantidad de trabajos que hay es de:", counter[k])


"""
4-      Mostrar los datos de todos los trabajos cuyo importe a cobrar sea mayor al importe promedio de todos los
 trabajos del arreglo

"""
def search(v):
    number = len(v)
    if number == 0:
        print("El arreglo está vacío.")
        return

    # PASO 1: Calcular el total de importes de TODOS los elementos
    add = 0
    for i in range(number):
        add += v[i].total

    # PASO 2: Calcular el promedio general
    prom = add / number
    print("El importe promedio general es de $", round(prom, 2))

    # PASO 3: Volver a recorrer para filtrar y mostrar los que superan el promedio
    print("\nTrabajos cuyo importe es mayor al promedio:")
    for i in range(number):
        if v[i].total > prom:
            print(v[i])



def principal():
    v = []
    option = -1
    while option !=5:
        print("Opcion 1: cargar el arreglo")
        print("Opcion 2: mostrar el arreglo con personal mayor a 3")
        print("Opcion 3: contar el arreglo y mostrar la cantidad de trabajos que ofrecen por tipo")
        print("Opcion 4: buscar el arreglo")
        print("Opcion 5: cerrar el arreglo")
        option = int(input("ingrese una opcion :"))
        if option == 1:
            charge()
        elif v:
            if option == 2:
                show(v)
            else:
                print("aun no se cargo el arreglo")
        elif v:
            if option == 3:
                count(v)
            else:
                print("aun no se cargo el arreglo")
            if option == 4:
                search(v)

            else:
                print("aun no se cargo el arreglo")
            if option == 5:
                print("programa terminado")




if __name__ == "__main__":
    principal()
