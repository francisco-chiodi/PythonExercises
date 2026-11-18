"""
La Cátedra de AED necesita un programa para controlar las notas finales los alumnos que aprobaron la materia. Por
cada alumno se conoce: legajo (un número entero), nombre y apellido, curso al que asistió (un entero entre 1 y 20),
nota final (un entero entre 6 y 10) y observaciones sobre el alumno (una cadena de caracteres terminada en "." con
palabras separadas con un blanco). Se pide desarrollar un programa que contenga mínimamente dos módulos y un
menú de opciones para las siguientes consignas:
1. Cargar un arreglo con los datos de n objetos de la clase Alumno de manera que en todo momento se
mantenga ordenado por legajo. Para esto debe utilizar el algoritmo de inserción ordenada con
búsqueda binaria (se considerará directamente incorrecta la solución basada en cargar el arreglo
completo y ordenarlo al final, o aplicar el algoritmo de inserción ordenada pero con búsqueda
secuencial). Valide la carga de n. Debe generar los datos en forma automática (con valores aleatorios).
2. Mostrar los datos del arreglo a razón de un alumno por línea. Indique al final del listado el porcentaje
de alumnos cuyo legajo es menor a un cierto valor l que se carga por teclado (no se requiere ninguna
validación respecto a este valor).
3. Informar la cantidad de alumnos que han sacado cada nota posible por cada curso (o sea, 5 * 20 = 100
contadores en una matriz de conteo), mostrando únicamente aquellos contadores que sean mayores a
cero.
4. Generar un archivo binario en el cual se graben los datos de todos los alumnos con nota superior al
promedio general, y que hayan cursado en el curso c, siendo c un valor que se carga por teclado.
5. Mostrar el archivo creado en el punto anterior, a razón de un alumno por línea en la pantalla.
6. Tome la cadena contenida en el campo observaciones del primer objeto del arreglo generado en el
punto 1, e indique cuántas palabras comienzan con una vocal (mayúscula o minúscula) que no sea la
"a", y no contienen ninguna “s” (mayúscula o minúscula). El texto debe ser procesado
obligatoriamente caracter a caracter, a razón de uno por vuelta de ciclo.
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
"""
import R4class
import pickle
import os

def average(quantity,total):
    return quantity//total

def percentage(quantity,total):
    return (quantity * 100)//total

def val(inf,message):
    n = int(input(message))
    while n <= inf:
        n = int(input(message))
    return n

def menu():
    "=== MENU DE OPCIONES ==="
    print("1. Cargue el vector")
    print("2. Muestre el vector")
    print("3. Generar matriz")
    print("4. Generar archivo binario")
    print("5. Mostrar archivo binario")
    print("0. Cerrar programa.")

def gen():
    legajo = R4class.legajo()
    nombre = R4class.nombre()
    curso = R4class.curso()
    nota = R4class.nota()
    observaciones = R4class.observaciones()
    record = R4class.catedra(legajo,nombre,curso,nota,observaciones)
    return record


def order(v,record):
    left = 0
    right = len(v) -1
    pos = 0
    while left <= right:
        mid = (left + right)//2
        if record.legajo == v[mid].legajo:
            pos = mid
            break
        if record.legajo > v[mid].legajo:
            left = mid + 1
        else:
            right = mid - 1

        if left > right:
            pos = left
    v[pos:pos] = [record]
    return v

"""
Indique al final del listado el porcentaje
de alumnos cuyo legajo es menor a un cierto valor l que se carga por teclado (no se requiere ninguna
validación respecto a este valor).
"""

def search(v,l):
    counter = 0
    total = len(v)
    for record in v:
        if record.legajo < l:
            counter += 1
    porc = percentage(counter,total)
    return print("el porcentaje es: ",porc)

"""
4. Generar un archivo binario en el cual se graben los datos de todos los alumnos con nota superior al
promedio general, y que hayan cursado en el curso c, siendo c un valor que se carga por teclado.
"""
def gen_bin(v,archive,c):
    total = 0
    quantity = 0
    m = open(archive,"wb")
    for i in v:
        total += 1
        quantity = quantity + i.nota
    prom = average(quantity,total)

    for record in v:
        if record.nota > prom and record.curso == c:
            pickle.dump(record,m)
    m.close()
"""
5. Mostrar el archivo creado en el punto anterior, a razón de un alumno por línea en la pantalla.
"""
def show_bin(archive):
    if os.path.exists(archive):
        m = open(archive,"rb")
        print("el archivo existe")
        size = os.path.getsize(archive)
        while m.tell() < size:
            record = pickle.load(m)
            print(record)
        m.close()

def show(v):
    for record in v:
        print(record)

def main():
    v = []
    menu()
    archive = "archive.dat"

    option = -1
    while option != 0:
        option = int(input("ingrese una opcion: "))
        if option == 1:
            n = val(0,"porfavor ingrese un numero mayor a 0: ")
            for i in range(n):
                record = gen()
                order(v,record)

        if option == 2:
            show(v)
            l = int(input("ingrese el valor menor a buscar en legajo: "))
            search(v,l)

        if option == 4:
            c = int(input("ingrese el numero del curso: "))
            gen_bin(v,archive,c)

        if option == 5:
            show_bin(archive)

if __name__ == "__main__":
        main()
