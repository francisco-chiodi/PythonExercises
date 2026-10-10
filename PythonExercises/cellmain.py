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
import pickle
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
    print("el vector ordenado es ")
    for i in range(n):
        print(v[i])

"""
3 - Generar un archivo binario con todas las líneas donde la cantidad de minutos consumidos superen un valor X ingresado
por teclado. Muestre dicho archivo a razón de un registro a la vez.
 al final indique que porcentaje representan las líneas del plan Y (y es la variable el plan es un numero
  ingresado por parámetro sobre el total de líneas del archivo.
"""

def gen_archive(v, x, archive_name="minutes.dat"):
    m = open(archive_name, "wb")
    for minutes in v:
        if minutes.quantity > x:
            pickle.dump(minutes, m)
    m.close()
    print("Archivo binario generado con éxito.")

#operar archivo

def show_percentage(y, archive_name = "minutes.dat"):
    if not os.path.getsize(archive_name):
        print("gordaso no existe el archivo, no se cumplen las condiciones.")
        return
    size = os.path.getsize(archive_name)
    if size == 0:
        print("el arvhivo esta vacio")
        return

    m = open(archive_name, "rb")
    total_lines = 0
    counter_y = 0
    while m.tell() < size: #m.tell() es un metodo que indica la posicion actual del puntero de lectura dentro del archivo.
        line = pickle.load(m) #Carga todo el archivo para imprimir linea por linea
        print(line)
        total_lines += 1
        if line.plan == y:
            counter_y += 1

    m.close()

    if total_lines > 0:
        percentage = (counter_y/total_lines) * 100
        print(f"las lineas del plan {y}, representan un total de {percentage:.2f} % sobre el total {total_lines}")
    else:
        print("no se pudo cargar el archivo")


"""
4 - Determinar e informar la cantidad de minutos consumidos por cada tipo de plan y en cada provincia a la que pertenece
esa línea. Son 460 contadores.
"""
def matrix(v):
    counter_matrix = 20 * [0] #son 19 indices pero el 0 cuenta entonces son 20 contadores.
    for index in range(20): #estructura matricial (plan) asignamos a cada fila una lista de 23 columnas cargadas en 0

        counter_matrix[index] = 23 * [0] #accedo a la matriz y cargo los contadores (provincias)

    for i in v: #accede directamente al vector
        f = i.plan
        c = i.location -1 #porque en el enunciado se toman desde 1 a 23, pero python lista desde 0 a 19
        counter_matrix[f][c] += i.quantity
    return counter_matrix

def show_matrix(counter_matrix):
    print("minutos consumidos por tipo de plan y provincia: ")
    data = False
    for f in range(20):
        for c in range(23): #22 provincias
            if counter_matrix[f][c] > 0:
                print(f" el plan {f} de la provincia  {c + 1} consumio en minutos {counter_matrix[f][c]}")
            data = True
    if not data:
        print("no hay datos cargados")

"""
5-Mostrar la línea con menor cantidad de minutos consumidos para las provincias x o y (donde ambos valores son ingre
sados por parámetro), en caso que haya mas de una mostrarlas a todas.
"""
def consume(x,y,v):
    lesser = 0
    for i in v:
        if i.location == x or i.location == y:
            if v.quantity > None and v.quantity > lesser:
                v.quantity = lesser
            print(f"la linea con menor cantidad de minutos consumidos para la provincia {i.location}, es {v[i]} con {lesser} miutos)

def main():
    v = []
    option = -1
    print("1. Cargar vector")
    print("2. Mostrar vector")
    print("3. Crear archivo, calcular y mostrar")
    print("4. Crear matriz")
    print("5. Econtrar los minimos minutos consumidos por provincia")
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

        if option == 3:
            if v:
                x = int(input("ingrese los minutos: "))
                gen_archive(v,x, "minutes.dat")
                y = int(input("ingrese el tipo del plan buscado para ver su porcentaje"))
                show_percentage(y, "minutes.dat")
            else:
                print("carge el vector primero")

        if option == 4:
            if v:
                m = matrix(v)
                show_matrix(m) #muestra casilleros >0

            else:
                print("cargue el vector")

        if option == 5:
            if v:
                x = int(input("seleccione una provincia"))
                y = int(input("seleccione otra provincia"))




#
if __name__ == "__main__":
    main()