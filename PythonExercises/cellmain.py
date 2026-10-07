"""
1. Empresa celulares
Una empresa dedicada a la venta de líneas para celulares nos pidió un programa que permita realizar una serie de i
nformes. De cada línea se sabe el número, el nombre del titular, el tipo de plan (valor de 0 a 19), la cantidad de
minutos consumidos, y la provincia donde se activó la línea (valor de 1 a 23).

Usted debe realizar dicho programa, controlado por un menú de opciones para que lleve a cabo los siguientes ítems:

1 - Cargar un vector de n Líneas, validando que el tamaño a cargar sea mayor a cero y que la provincia y tipo de plan
sean válidos. El arreglo debe generarse en forma ordenada por numero.

2 - Listar todas las líneas a razón de un registro por vez.

3 - Generar un archivo binario con todas las líneas donde la cantidad de minutos consumidos superen un valor X ingresado
por teclado. Muestre dicho archivo a razón de una registro a la vez y al final indique que porcentaje representan las
líneas del plan Y ingresado por parámetro sobre el total de líneas del archivo.

4 - Determinar e informar la cantidad de minutos consumidos por cada tipo de plan y en cada provincia a la que pertenece
esa línea. Son 460 contadores.

5 - Mostrar la línea con menor cantidad de minutos consumidos para las provincias x o y (donde ambos valores son ingre
sados por parámetro), en caso que haya mas de una mostrarlas a todas.

6 - Buscar una línea x ingresada por teclado. Si existe incrementar sus minutos consumidos en un 20% y mostrar los datos
de la línea. Caso contrario indicar con un mensaje que no existe.
"""
import cellclass
import os
import random
def validate(inf):
    n = int(input("ingrese un numero mayor a 0: "))
    while n <= inf:
        n = int(input("error. ingrese un numero mayor a 0: "))
    return n

"""
1. Empresa celulares
Una empresa dedicada a la venta de líneas para celulares nos pidió un programa que permita realizar una serie de i
nformes. De cada línea se sabe el número, el nombre del titular, el tipo de plan (valor de 0 a 19), la cantidad de
minutos consumidos, y la provincia donde se activó la línea (valor de 1 a 23).
"""
def charge():
    n = validate(0)
    v = n * [None]
    names = ("lain","fran","bit","lovethewayyouhate","sofi","zaira", "juliana", "melanie", "victoria,", "joaquin",
             "fer", "celeste", "fabricio","sebastian","lucas","julieta","i_miss_you","love_the_way_you_hate","hell")
    for i in range(len(v)):
        num = random.randint(1000000,9999999)
        name = random.choice(names)
        types = random.randint(0,19)
        quantity = random.randint(1,60)
        location = random.randint(1,23)
        v[i] = cellclass.Cellclass(num,name,types,quantity,location)
    return v

"""
1 - Cargar un vector de n Líneas, validando que el tamaño a cargar sea mayor a cero y que la provincia y tipo de plan
sean válidos. El arreglo debe generarse en forma ordenada por numero.

2 - Listar todas las líneas a razón de un registro por vez.
"""
def show(v):
    n = len(v)
    for i in range(n-1):
        for j in range(i+1,n):
            if v[i].num > v[j].num:
                v[i], v[j] = v[j],v[i]
            print("el vector ordenado por numero es: ")

    for i in range(n):




def main():
    v = []
    option = -1
    print("1. Cargar vector")
    print("2. Mostrar vector")
    print("6. Cerrar programa")
    while option != 6:
        option = int(input("porfavor, ingrese una opcion: "))
        if option == 1:
            v = charge() #NO TE OLVIDES DE CARGAR A V
        print("vector cargado" )
        if option == 2:
            if v:
                show(v)
            else:
                print("vector no cargado")

#
if __name__ == "__main__":
    main()