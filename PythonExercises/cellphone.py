"""
1. Empresa celulares
Una empresa dedicada a la venta de líneas para celulares nos pidió un programa que permita realizar una serie de informes.
 De cada línea se sabe el número, el nombre del titular, el tipo de plan (valor de 0 a 19),
  la cantidad de minutos consumidos, y la provincia donde se activó la línea (valor de 1 a 23).
Usted debe realizar dicho programa, controlado por un menú de opciones para que lleve a cabo los siguientes ítems:
1 - Cargar un vector de n Líneas, validando que el tamaño a cargar sea mayor a cero y que la provincia y tipo de plan sean
válidos.

El arreglo debe generarse en forma ordenada por numero.


3 - Generar un archivo binario con todas las líneas donde la cantidad de minutos consumidos superen un valor X ingresado por teclado.
Muestre dicho archivo a razón de una registro a la vez y al final indique que porcentaje representan las líneas del plan Y ingresado
por parámetro sobre el total de líneas del archivo.

4 - Determinar e informar la cantidad de minutos consumidos por cada tipo de plan y en cada provincia a la que pertenece esa línea. Son
 460 contadores.

5 - Mostrar la línea con menor cantidad de minutos consumidos para las provincias x o y (donde ambos valores son ingresados por parámetro)
, en caso que haya mas de una mostrarlas a todas.

6 - Buscar una línea x ingresada por teclado. Si existe incrementar sus minutos consumidos en un 20% y mostrar los datos de la línea. Caso
 contrario indicar con un mensaje que no existe.

"""
import random
import cellclass

def validate():

    n = int(input("ingrese los elementos del vector"))
    while n <= 0:
        n = int(input("error, ingrese un numero mayor a 0"))
    return n

"""
Una empresa dedicada a la venta de líneas para celulares nos pidió un programa que permita realizar una serie de informes.
 De cada línea se sabe el número, el nombre del titular, el tipo de plan (valor de 0 a 19),
  la cantidad de minutos consumidos, y la provincia donde se activó la línea (valor de 1 a 23).
"""

def charge(v):
    n = validate()
    v = n * [None]
    nombres = ("cami","juli","fran","lain","juan","mica","anahi","sofi","loveher","kurt","kira","freeman")
    for i in range(len(v)):
        num = random.randint(1000000,9000000)
        name = random.choice(nombres)
        plan = random.randint(0,19)
        minutes = random.randint(1,120)
        location = random.randint(1,23)
        v[i] = cellclass.Cell(num,name,plan,minutes,location)
    return v

def show(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i+1,n):
            if v[i].num > v[j].num:
                v[i],v[j] = v[j],v[i]


        print(v[i])


def main():
    v = []
    option = -1
    while option != 5:
        print("1. Cargar")
        print("2. Mostrar")
        print("5. Cerrar")
        option = int(input("Ingrese una opcion: "))
        if option == 1:
           v = charge(v)
        if option == 2:
            show(v)
        if option == 5:
            print("fin")

if __name__ == "__main__":
    main()