"""Turno 1
 Enunciado: La Secretaría de Tecnología de una ciudad inteligente se encuentra d
  iseñando un sistema para el control de su infraestructura digital, por lo que necesitan un programa que les permita g
  estionar la información de los sensores distribuidos en la vía pública. Por cada Sensor se conoce: código de identifi
  cación (cadena de caracteres, combinación de números y letras, por ejemplo SEN001A), ubicación donde se encuentra ins
  talado (cadena de caracteres, por ejemplo Av. Colón y General Paz), tipo de magnitud que evalúa (entero de 1 a 21, po
  r ejemplo 1-Calidad del aire, 2-Flujo vehicular, 3-Estación meteorológica, etc), estado operativo (booleano, si el
   atributo “operativo” es igual a True indica que el sensor se encuentra activo y transmitiendo y, si el atributo
   “operativo” vale False indica que se encuentra fuera de servicio) y consumo energético (decimal, expresado en watts,
    entre 15.5 y 50). Se pide desarrollar un programa en Python controlado por un menú de opciones, que posea como mínim
    o dos módulos, y que permita gestionar las siguientes tareas:  1. Cargar el arreglo pedido con los datos de los n s
    ensores, donde n es un valor ingresado por teclado. Debe asegurar que los datos sean siempre correctos. Todos los c
    ampos deben ser generados de manera automática, con valores aleatorios.  2. Mostrar los datos de todos los sensores
     que se encuentren fuera de servicio, a razón de uno por línea, ordenados por consumo energético de mayor a menor.
     Al finalizar, mostrar el promedio de consumo energético de dichos sensores.
      3. Determinar cuántos sensores activo
     s (atributo operativo vale True) hay por cada tipo de magnitud (21 contadores). Mostrar solamente los contadores m
     ayores a cero. 4. Determinar si existe un sensor con una dirección d y que esté en estado operativo activo (d se ca
     rga por teclado, sin exigencia de validación). Si lo encuentra, muestre todos los datos del sensor, y modifique su
     consumo energético haciéndole una disminución del 5%, finalmente vuelva a mostrar todos los datos del objeto modifi
     cado. Si no lo encuentra, informe con un mensaje que no existe. Debe detener la búsqueda en el primero que encuentre
      (sin importar si hay más de un objeto que cumpla el criterio pedido).
Criterios generales de evaluación."""
import class24
import random


def validate(inf):
    number = int(input("ingrese un numero mayor a " + str(inf)))
    while number <= inf:
        number = int(input("error, porfavor ingrese un numero mayor a " + str(inf)))
    return number
"""
    def __init__(self,code,ubi,magnitude,state,con):
     Por cada Sensor se conoce: código de identifi
  cación (cadena de caracteres, combinación de números y letras, por ejemplo SEN001A),
   ubicación donde se encuentra instalado (cadena de caracteres, por ejemplo Av. Colón y General Paz), 
   tipo de magnitud que evalúa (entero de 1 a 21, por ejemplo 1-Calidad del aire, 2-Flujo vehicular, 3-Estación meteorológica, etc)
   , estado operativo (booleano, si el
   atributo “operativo” es igual a True indica que el sensor se encuentra activo y transmitiendo y, si el atributo
   “operativo” vale False indica que se encuentra fuera de servicio) y
    consumo energético (decimal, expresado en watts,
    entre 15.5 y 50).

"""



def charge(v):
    number = validate(0)
    v = number * [None]
    letters = ("A","B","C","D","E","F","G")
    numbers = ("13","11","99","21","17","27")
    ubi = ("general paz","av.colon","carlos paz","sagrada familia", "juan v.just", "santa fe")
    for i in range(number):
        code = random.choice(letters) + random.choice(numbers)
        ubi = random.choice(ubi)
        magnitude = random.randint(1,21)
        state = random.choice(True,False)
        con = round(random.uniform(15.5,50),2)

    return v

def show(v):
    number = len(v)

    # 1. ORDENAR TODO EL VECTOR por consumo de mayor a menor
    for i in range(number - 1):
        for j in range(i + 1, number):
            if v[i].con < v[j].con:
                v[i], v[j] = v[j], v[i]

    # Variables para acumular y contar SOLO los fuera de servicio
    add = 0
    counter = 0

    print("\nSensores fuera de servicio (ordenados de mayor a menor consumo):")

    # 2. MOSTRAR Y ACUMULAR únicamente los que estén fuera de servicio (state == False)
    for k in range(number):
        if v[k].state == False:   # O también: if not v[k].state:
            print(v[k])
            add += v[k].con
            counter += 1

    # 3. CALCULAR PROMEDIO de esos sensores mostrados
    if counter > 0:
        prom = add / counter
        print("El promedio de consumo de los sensores fuera de servicio es:", round(prom, 2), "Watts")
    else:
        print("No se encontraron sensores fuera de servicio.")

def principal():
    v = []
    option = -1
    while option !=5:
        print("1. cargar")
        print("2. mostrar")
        print("3. buscar")
        print("4. contar")
        print("5. salir")
        option = int(input("ingrese una opcion"))
        if option == 1:
            charge()
        elif option == 2:
            if v:
                show()
            else:
                print("aun no se ha cargado el vector ")
                option = int(input("ingrese una opcion"))
        elif option == 3:
            if v:
                search()
            else:
                print("aun no se ha cargado el vector ")
                option = int(input("ingrese una opcion"))
        elif option == 4:
            if v:
                count()
            else:
                print("aun no se ha cargado el vector ")
                option = int(input("ingrese una opcion"))
        elif option == 5:
            print("programa finalizado")
if __name__ == "__main__":
    principal()