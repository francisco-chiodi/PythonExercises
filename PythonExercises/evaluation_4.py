"""Un estudio de abogados desea un sistema para procesar los datos de los juicios que tiene en su cartera. Por cada
Juicio se conoce su código de expediente (un número entero)
, la descripción o carátula del juicio (una cadena),
el tipo de juicio (un entero entre 1 y 15),
el nombre del cliente defendido,
y el monto de honorarios a cobrar por ese juicio.
 Se desea almacenar la información referida a los n juicios en un arreglo de objetos de tipo Juicio (definir el
tipo Juicio y cargar n por teclado). Se pide desarrollar un programa en Python controlado por un menú de
opciones, en el que se incluyan como mínimo dos módulos, para permita gestionar las siguientes tareas:
a. Cargar el arreglo pedido con los datos de los n juicios. Valide o asegure que los datos cargados sean correctos.
Puede hacer la carga en forma manual, o puede generar los datos en forma automática (con valores
aleatorios). Pero al menos una debe programar. Pero si hace carga automática, todos los campos deben ser
cargados así (no combine ambas técnicas en la carga de un objeto).

b. Mostrar datos de todos los juicios cuyo monto de honorarios sea mayor a mon (que se carga por teclado), en
un listado ordenado de menor a mayor según la descripción o carátula, a razón de un juicio por línea. Al final
del listado, indique cuántos objetos se mostraron.

c. Determinar y mostrar la cantidad de juicios que hay por cada posible tipo (15 contadores en un vector de
conteo). Mostrar sólo aquellos contadores que sean mayores a una cantidad c ingresada por teclado.

d. Determinar si existe un juicio cuyo código de expediente sea igual a cod. Si existe alguno, modificar el monto
de honorarios de ese objeto tomando el nuevo valor por teclado, y mostrar los datos de ese juicio incluyendo
esa modificación. Si no existe, informar con un mensaje. Debe mostrar los datos del primero que encuentre, y
detener la búsqueda en el primero que encuentre (sin importar si hay más de un objeto que cumpla el criterio
pedido)."""
import random
import class_4
def validate(inf):
    number = int(input("ingrese el numero porfavor: "))
    while number <= inf:
        print("error. porfavor, ingrese nuevamente el numero: ")
        number = int(input("ingrese el numero porfavor: "))
    return number

def charge():
    number = validate(0)
    v = number * [None]
    descriptions = ("A","B","C","D","E","F","G","H","I")
    name = ("lain","fran","zaira","juliana","melanie","victoria")
    last_name = ("Díaz", "Giuliani", "Trejo", "Masiero", "Duplesis", "Johnson", "Iriarte")

    for i in range(number):
        exp_code = random.randint(1,5000)
        des = random.choice(descriptions)
        type = random.randint(1,15)
        name = random.choice(name) + random.choice(last_name)
        total =round(random.uniform(30000,60000),2)
        v[i] = class_4.Service(exp_code,des,name,type,total)
    return(v)

"""b. Mostrar datos de todos los juicios cuyo monto de honorarios sea mayor a mon (que se carga por teclado), en
un listado ordenado de menor a mayor según la descripción o carátula, a razón de un juicio por línea. Al final
del listado, indique cuántos objetos se mostraron."""

def show(v):
    number = len(v)
    for i in range(number-1):
        for j in range(i+1,number):
            if v[i].des > v[j].des:
                v[i],v[j] = v[j],v[i]
    mon = int(input("ingrese el filtro de monto minimo a buscar: "))

    counter = 0
    print("Listado de juicios con honorarios mayores a", mon, ":")
    for k in range(number):
        if v[k].total > mon: #Compara el atributo del objeto en la posición 'k' con el valor 'mon'
            counter += 1
            print(v[k])
    print("se mostraron",counter,"objetos")


"""
c. Determinar y mostrar la cantidad de juicios que hay por cada posible tipo (15 contadores en un vector de
conteo). Mostrar sólo aquellos contadores que sean mayores a una cantidad c ingresada por teclado.
"""


def count(v):
    number = len(v)
    counter_type = 15 * [0]

    # 1. Contar los juicios por tipo
    for i in range(number):
        index = v[i].type - 1
        counter_type[index] += 1

    # 2. Pedir por teclado la cantidad mínima 'c' a superar
    c = int(input("Ingrese la cantidad mínima 'c' a superar para filtrar: "))

    print("Tipos de juicios con más de", c, "casos:")

    # 3. Filtrar usando 'c' y mostrar la casilla correspondiente
    for k in range(15):
        if counter_type[k] > c:  # Compara el conteo contra 'c'
            print("El tipo de juicio", k + 1, "tiene una cantidad de:", counter_type[k])

"""Determinar si existe un juicio cuyo código de expediente sea igual a cod. Si existe alguno, modificar el monto
de honorarios de ese objeto tomando el nuevo valor por teclado, y mostrar los datos de ese juicio incluyendo
esa modificación. Si no existe, informar con un mensaje. Debe mostrar los datos del primero que encuentre, y
detener la búsqueda en el primero que encuentre (sin importar si hay más de un objeto que cumpla el criterio
pedido)"""


def search(v):
    number = len(v)
    cod = int(input("Ingrese codigo de expediente a buscar: "))

    for i in range(number):
        if v[i].exp_code == cod:
            print("Encontrado. Datos actuales:")
            print(v[i])

            # Pedimos el nuevo valor por teclado y actualizamos el honorario/monto
            new_amount = float(input("Ingrese el nuevo monto de honorarios: "))
            v[i].total = new_amount

            print("Datos actualizados:")
            print(v[i])
            return  # Corta la función y detiene la búsqueda inmediatamente

    # Si terminó todo el for y nunca entró al return:
    print("No se encontro un juicio con ese codigo de expediente.")


def principal():
    v = []
    option = -1
    while option != 5:
        print("1. cargar el arreglo")
        print("2. mostrar ordenado")
        print("3. contar por tipo")
        print("4. buscar")
        print("5. salir")
        option = int(input("eliga una opcion: "))
        if option == 1:
            v = charge()
            print("arreglo cargado exitosamente")
        elif option == 2:
            if v:
                show(v)
            else:
                print("el vector no fue cargado")

        elif option ==3:
            if v:
                count(v)
            else: print("el vector no fue cargado")

        elif option == 4:
            if v:
                search(v)
            else: print("el vector no fue cargado")

        elif option == 5:
            print("fin del programa")



if __name__ == "__main__":
    principal()