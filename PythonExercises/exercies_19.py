"""

2. Triatlon
El Comité Argentino de Atletismo llevo a cabo una prueba atlética de Triatlón, nos solicito un programa que valide lo
 anotado por los jueces del evento, para dicho propósito se deben cargar los datos de los tres atletas con
 mejor promedio. De cada atleta se conocen Nombre, Tiempo Natación, Tiempo Ciclismo, Tiempo Corriendo
  (todo en minutos para simplificar los cálculos).

Usted debe:
Informar tiempo promedio de cada competidor
Determinar el podio, indicando el nombre del primer, segundo y tercer mejor promedio
"""
import exercices_class
import random

def average(tiempo_natacion,tiempo_ciclismo,tiempo_corriendo):
    add = 0
    add = tiempo_natacion + tiempo_ciclismo + tiempo_corriendo
    return add/3


def validate():
    number = int(input("Ingrese un tiempo mayor a 0: "))
    while number <= 0:
        print("Error. El número debe ser mayor a 0.")
        number = int(input("Ingrese un tiempo mayor a 0: "))
    return number

def charge():
    v = []
    print("porfavor, cargue los datos de los tres atletas con mejor promedio: ")

    for i in range(3):
        nombre = input("Nombre: ")
        tiempo_natacion = validate()
        tiempo_ciclismo = validate()
        tiempo_corriendo = validate()
        atleta = exercices_class.Exercise(nombre,tiempo_natacion,tiempo_ciclismo,tiempo_corriendo)
        v.append(atleta)

    print("arreglo cargado")
    return v

def show(v):
    print("promedio de los competidores")
    for atleta in v:
        prom = average(atleta.time_nat, atleta.time_cic,atleta.time_run)
        print(f"El atleta {atleta.name} tiene un promedio de {prom:.2f} min ")

def principal():
    v=[]
    option = -1

    while option !=3:

        print("1. cargar datos ")
        print("2. mostrar datos ")
        print("3. cerrar programa")
        option = int(input("ingrese una opcion: "))
        if option == 1:
            v = charge()
        elif option == 2:
            if v:
                show(v)
            else:
                print("carge el vector")
        elif option == 3:
            print("programa finalizado")






if __name__ == "__main__":
    principal()
