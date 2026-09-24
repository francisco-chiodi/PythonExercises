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
import random
import exercices_class



def charge():
    v = 3 * [None]
    name_tuple = ("lain","juli","fran","kira","anahi","fabri","sebastian","ada")
    for i in range(3):
        nom = random.choice(name_tuple)
        time_nat = random.randint(5,10)
        time_cic = random.randint(5,10)
        time_run = random.randint(5,10)
        v[i] = exercices_class.Exercise(nom,time_nat,time_cic,time_run)
    return v

def show(v):
    n = len(v)
    print("listado de competidores")
    for i in range(n):
        average = (v[i].time_nat + v[i].time_cic + v[i].time_run)/3
        print(v[i], f"promedio: {average:.2f} min")



def principal():

    v = []
    option = -1
    while option !=3:
        print("1. cargar")
        print("2. mostrar")
        print("3. cerrar")

        option = int(input("ingrese una opcion:"))
        if option == 1:
           v = charge()
        if option == 2:
            show(v)

        if option == 3:
            print("finalizado")

if __name__ == "__main__":
    principal()

