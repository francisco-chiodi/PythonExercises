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
import R1class

def validate(inf,message):
    n = int(input(message))
    while n <= inf:
        n = int(input("porfavor, que sea mayor a 0: "))
    return n

def valrange(inf,sup,message):
    n = -1
    while n != -5:
        n = int(input(message))
        if n < inf or n > sup:
            n = int(input("que sea entre 1 y 5: "))
    return n

def charge(v):
    n = validate(0,"cargue un numero mayor a 0: ")
    v = n * [None]
    for i in range(n):
        ide = R1class.id_gen()
        name = R1class.name_gen()
        addr = R1class.addres_gen()
        employee = R1class.employee_gen()
        tribute = R1class.tribute_gen()
        v[i] = R1class.r1(ide,name,addr,employee,tribute)
    return v



def show(v):

    for i in v:
        print(f"los vectores son: {i}")

def main():
    v = []
    print("porfavor ingrese una opcion: \n"
          "1: cargar vector\n"
          "2: mostrar vector\n")
    option = -1
    while option != 5:
        option = int(input("ingrese una opcion: "))
        if option == 1:
           v = charge(v)
           print("vector cargado")

        elif option == 2:
            show(v)


if __name__ == "__main__":
    main()
