"""
Una municipalidad mantiene un listado de los distintos comercios que hay en su ciudad. Por cada comercio se
conoce: el identificador (un número entero), el nombre del mismo (una cadena de caracteres), su dirección
(una cadena de caracteres terminada en "." y con palabras separadas por un blanco), la cantidad de
empleados que trabajan en él y el monto anual que paga de impuestos. Se pide desarrollar un programa que
contenga mínimamente dos módulos y un menú de opciones para las siguientes consignas:
1. Cargar un arreglo de objetos con los datos de n objetos de la clase Comercio de manera que en todo
momento se mantenga ordenado por nombre. Para esto debe utilizar el algoritmo de inserción
ordenada con búsqueda binaria (se considerará directamente incorrecta la solución basada en cargar
el arreglo completo y ordenarlo al final, o aplicar el algoritmo de inserción ordenada pero con
búsqueda secuencial). Valide la carga del valor n. Debe generar los datos en forma automática (con
valores aleatorios).
2. Mostrar los datos del arreglo a razón de un comercio por línea. Indique al final del listado la cantidad
total de trabajadores que trabajan entre todos los comercios que se mostraron.
3. Guardar en un archivo binario todos los comercios cuyo monto anual de impuestos esté comprendido
entre i1 e i2 (dos valores que se cargan por teclado y sobre los que no se requiere ninguna validación).
4. Mostrar el archivo generado en el punto anterior. Muestre al final del listado la cantidad promedio de
trabajadores que trabajan en los comercios mostrados.
5. Buscar en el arreglo generado en el punto 1 un comercio cuyo nombre sea nom (un valor ingresado
por teclado). Si el comercio se encuentra en el vector, mostrar sus datos y retornar el título del mismo
para utilizar luego en el ítem 6. Si el artículo no se encuentra, mostrar el mensaje "El comercio no
existe, llame al (111) 0303456 para mayor detalle.", y retornar ese mismo mensaje para ser usado en
el punto 6.
6. Procesar la cadena resultante del punto 5 para responder la siguiente pregunta: ¿Cuál es la cantidad de
palabras de esa cadena que contienen, al menos, 2 dígitos impares y ningún 0? El texto debe ser
procesado obligatoriamente caracter a caracter, a razón de uno por vuelta de ciclo.
Criterios generales de evaluación:
a.) Desarrollo del programa completo, incluyendo el menú correctamente planteado, funciones
correctamente diseñadas y parametrizadas (cuando sea apropiado) y validaciones: [máximo: 1.5
puntos (10% del puntaje)]
b.) Desarrollo correcto de los ítems 1 y 2: [máximo: 3 puntos (20% del puntaje)]
c.) Desarrollo correcto del ítem 3: [máximo: 3 puntos (20% del puntaje)]
d.) Desarrollo correcto del ítems 4: [máximo: 3 puntos (20% del puntaje)]
e.) Desarrollo correcto del ítem 5: [máximo: 3 puntos (20% del puntaje)]
f.) Desarrollo correcto del ítem 6: [máximo: 1.5 puntos (10% del puntaje), pero resta si deja en blanco]
Para llegar a una calificación de 4 (requerida para regularizar), el alumno debe llegar a un total acumulado
de al menos 55% del puntaje (es decir, alrededor de 8.25 puntos acumulados). Y para llegar a una
calificación de 7 (requerida como mínimo para intentar aprobar/promocionar), el alumno debe llegar a un
total acumulado de al menos 69% del puntaje (es decir, alrededor de 10.35 puntos acumulados).
Cargar un arreglo de objetos con los datos de n objetos de la clase Comercio de manera que en todo
momento se mantenga ordenado por nombre. Para esto debe utilizar el algoritmo de inserción
ordenada con búsqueda binaria (se considerará directamente incorrecta la solución basada en cargar
el arreglo completo y ordenarlo al final, o aplicar el algoritmo de inserción ordenada pero con
búsqueda secuencial). Valide la carga del valor n. Debe generar los datos en forma automática (con
valores aleatorios).
"""
"""
1. Cargar un arreglo de objetos con los datos de n objetos de la clase Comercio de manera que en todo
momento se mantenga ordenado por nombre. Para esto debe utilizar el algoritmo de inserción
ordenada con búsqueda binaria (se considerará directamente incorrecta la solución basada en cargar
el arreglo completo y ordenarlo al final, o aplicar el algoritmo de inserción ordenada pero con
búsqueda secuencial). Valide la carga del valor n. Debe generar los datos en forma automática (con
valores aleatorios).
"""
import  R1class
import os
import pickle

def val(inf,message):
    n = int(input(message))
    while n < inf:
        n = int(input("porfavor, que sea mayor a 0"))
    return n

def create(v,n):
    for i in range(n):
        iden = R1class.id_gen()
        name = R1class.name_gen()
        addr = R1class.addres_gen()
        employees = R1class.employee_gen()
        tribute = R1class.tribute_gen()
        record = R1class.r1(iden,name,addr,employees,tribute)
        charge_order(v,record)

"""
2. Mostrar los datos del arreglo a razón de un comercio por línea. Indique al final del listado la cantidad
total de trabajadores que trabajan entre todos los comercios que se mostraron.
"""

"""
3. Guardar en un archivo binario todos los comercios cuyo monto anual de impuestos esté comprendido
entre i1 e i2 (dos valores que se cargan por teclado y sobre los que no se requiere ninguna validación).
"""


def gen(v,i1,i2,archive):
    m = open(archive,"wb")
    for request in v:
        if request.tribute >= i1 and request.tribute <= i2:
            pickle.dump(request,m)
    m.close()

"""
4. Mostrar el archivo generado en el punto anterior. Muestre al final del listado la cantidad promedio de
trabajadores que trabajan en los comercios mostrados.
"""

def average(total,quantity):
    return total//quantity

def show_file(archive):
    total = 0
    quantity = 0
    if not os.path.exists(archive):
        print("el archivo no se genero")
        return
    size = os.path.getsize(archive)
    print("el tamano es ", size)
    if size == 0:
        print("el archivo esta vacio")
    else:
        m = open(archive,"rb")
        while m.tell() < size:
            record = pickle.load(m)
            total += record.employees
            quantity += 1 #un simple contador para el comercio
            print("lista: ", record)

        prom = average(total,quantity)

        m.close()
        print("promedio: ",prom)

"""
5. Buscar en el arreglo generado en el punto 1 un comercio cuyo nombre sea nom (un valor ingresado
por teclado). Si el comercio se encuentra en el vector, mostrar sus datos y retornar el título del mismo
para utilizar luego en el ítem 6. Si el artículo no se encuentra, mostrar el mensaje "El comercio no
existe, llame al (111) 0303456 para mayor detalle.", y retornar ese mismo mensaje para ser usado en
el punto 6.
"""

def search(v,nom):
    for record in v:
        if record.name == nom:
            print("se encontro el nombre: ", record)
            return nom

    message = "El comercio no existe, llame al (111) 0303456 para mayor detalle."
    print(message)

    return message

def show(v):

    accumulator = 0
    for record in v:
        print("el vector es:",record)

        accumulator += record.employees

    print("la cantidad de empleados es", accumulator)
    return accumulator


def charge_order(v,record):
    left = 0
    right = len(v) -1
    pos = 0
    while left <= right:
        mid = (left+right)//2
        if record.name == v[mid].name:#estas ordenando el vector por eso lo comparas contra si mismo
            pos = mid
            break

        if record.name < v[mid].name:
            right = mid -1
        else:
            left = mid + 1

        if left > right:
            pos = left
    v[pos:pos] = [record]
    return v

"""
6. Procesar la cadena resultante del punto 5 para responder la siguiente pregunta: ¿Cuál es la cantidad de
palabras de esa cadena que contienen, al menos, 2 dígitos impares y ningún 0? El texto debe ser
procesado obligatoriamente caracter a caracter, a razón de uno por vuelta de ciclo.
    "El comercio no existe, llame al (111) 0303456 para mayor detalle."

"""
def word(function):
    digits = "0123456789"
    numbers = 0
    letters = 0
    for char in function:
        if char not in " .,":
            letters += 1
            if char in digits:
                if len(char) % 2 != 0 and char != "0":
                    numbers +=1
    print("letras",letters)
    print("numeros", numbers)



def main():
    v = []
    print("1. Cargar y ordenar")
    print("2. mostrar")
    print("3. Crear binario")
    print("4. mostrar promedio")
    print("5. Buscar por nombre")
    print("6. Procesar palabra")


    option = -1
    while option != 6:
        option = int(input("ingrese una opcion: "))

        if option == 1:
            n = val(0, "ingrese un numero mayor a 0: ")
            create(v,n)

        if option == 2:
            show(v)

        if option == 3:
            archive = "name.dat"
            i1 = int(input("ingrese el impuesto minimo"))
            i2 = int(input("ingrese el impuesto maximo"))
            gen(v,i1,i2,archive)

        if option == 4:
            show_file(archive)

        if option == 5:
            nom = input("ingrese el nombre: ")
            function = search(v,nom)

        if option == 6:
            word(function)

if __name__ == "__main__":
    main()