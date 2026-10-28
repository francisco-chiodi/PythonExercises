"""
1. Empresa celulares
Una empresa dedicada a la venta de líneas para celulares nos pidió un programa que permita realizar una serie de
 informes. De cada línea se sabe el número, el nombre del titular, el tipo de plan (valor de 0 a 19), la cantidad de
 minutos consumidos, y la provincia donde se activó la línea (valor de 1 a 23).

Usted debe realizar dicho programa, controlado por un menú de opciones para que lleve a cabo los siguientes ítems:

1 - Cargar un vector de n Líneas, validando que el tamaño a cargar sea mayor a cero y que la provincia y tipo de plan
 sean válidos. El arreglo debe generarse en forma ordenada por numero.

2 - Listar todas las líneas a razón de un registro por vez.

3 - Generar un archivo binario con todas las líneas donde la cantidad de minutos consumidos superen un valor X
ingresado por teclado. Muestre dicho archivo a razón de una registro a la vez y al final indique que
porcentaje representan las líneas del plan Y ingresado por parámetro sobre el total de líneas del archivo.

4 - Determinar e informar la cantidad de minutos consumidos por cada tipo de plan y en cada provincia a la que
 pertenece esa línea. Son 460 contadores.

5 - Mostrar la línea con menor cantidad de minutos consumidos para las provincias x o y (donde ambos valores
son ingresados por parámetro), en caso que haya mas de una mostrarlas a todas.

6 - Buscar una línea x ingresada por teclado. Si existe incrementar sus minutos consumidos en un 20% y mostrar
 los datos de la línea. Caso contrario indicar con un mensaje que no existe
"""
import ceclass
import random
import os
import pickle
"""
Una empresa dedicada a la venta de líneas para celulares nos pidió un programa que permita realizar una serie de
 informes. De cada línea se sabe el número, el nombre del titular, el tipo de plan (valor de 0 a 19), la cantidad de
 minutos consumidos, y la provincia donde se activó la línea (valor de 1 a 23).
"""
def validate(inf,message):
    n = int(input(message))
    while n <= inf:
        n = int(input("porfavor, que el numero sea mayor a 0: "))
    return n

def charge(v,n):
    for i in range(n):
        number = ceclass.num_gen()
        name =  ceclass.name_gen()
        type_plan = random.randint(0,19)
        ammount = random.randint(1,120)
        location = random.randint(1,23)
        record = ceclass.Cel(number,name,type_plan,ammount,location)
        add_order(v,record)

def add_order(v,record):
    left = 0
    pos = 0
    right = len(v) -1
    while left <= right:
        mid = (left + right)//2
        if v[mid].number == record.number:
            pos = mid
            break
        if record.number < v[mid].number:
            right = mid - 1
        else:
            left = mid + 1
    if left > right:
        pos = left
    v[pos:pos] = [record]

def show(v):
    lines = ceclass.header()
    for record in v:
        lines += str(record)
    print(lines)

def val_range(mini,maxi,message):
    n = mini -1
    while n < mini or n > maxi:
        if n < mini or n > maxi:
            n = int(input(message))
    return n


def percentage(contador,total):
    porcentaje = 0
    if total >0:
        porcentaje = contador * 100 / total
    return porcentaje

def binary(v,filename,x):
    m = open(filename,"wb")
    lines = ceclass.header()
    for record in v:
        if record.quantity > x:
            lines += str(record)
            pickle.dump(record,m)
    m.close()
    print(f"{lines}")

def readbinary(filename, y):

    if not os.path.exists(filename):
        print(f"{filename} no existe")
        return
    m = open(filename,"rb")
    size = os.path.getsize(filename)
    total = 0
    contador = 0
    lines = ceclass.header()
    while m.tell() < size:
        record = pickle.load(m)

        if record.type_plan == y:
            contador += 1
            lines += str(record)
        porcentaje = percentage(contador,total)
    m.close()
    print(f"{lines} representan el {porcentaje}")

"""
6 - Buscar una línea x ingresada por teclado. Si existe incrementar sus minutos consumidos en un 20% y mostrar
 los datos de la línea. Caso contrario indicar con un mensaje que no existe
"""
def search(v,x):
    left = 0
    right = len(v) - 1
    pos = -1
    while left <= right:
        mid = (left + right)//2
        if v[mid].number == x:
            pos = mid
            break
        if x < v[mid].number:
            right =  mid - 1
        else:
            left = mid + 1
    return pos

def main():
    v = []
    print("1. Cargar vector")
    print("2. Mostrar vector")
    print("3. Cargar vector y operar")
    print("4. Buscar vector y operar")
    print("5. Cerrar vector")
    option = -1
    while option !=5:
        option = val_range(1,5,"el rango de seleccion es entre 1 y 5: ")
        if option == 1:
            n =  validate(0,"porfavor, ingrese un numero mayor a 0: ")
            charge(v,n)
        elif option == 2:
            if len(v) > 0:
                show(v)
        elif option == 3:
            filename = "binary.dat"
            x = int(input("ingrese minutos: "))
            binary(v,filename,x)
            y = int(input("ingrese el numero del plan: "))
            readbinary(filename,y)

        elif option == 4:
            if len(v) > 0:
                x = input("ingrese numero de linea")
                pos = search(v,x)
                lines = ceclass.header()
                if pos != -1:
                    total = v[pos].quantity * 0.20
                    v[pos].quantity += total
                    lines+= str(v[pos])
                    print(f"{lines}")


            """
            6 - Buscar una línea x ingresada por teclado. Si existe incrementar sus minutos consumidos en un 20% y mostrar
             los datos de la línea. Caso contrario indicar con un mensaje que no existe
            """




if __name__ == "__main__":
    main()