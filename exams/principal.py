import os.path
import pickle
import random
"""
Turno T4 - Enunciado:
Los oganizadores del festival de Lollapalooza han requerido un programa para gestionar
 los datos de las distintas bandas/cantantes que tiene previsto que se presenten. Por 
 cada Banda se conoce: Nombre de la banda/cantante (cadena de caracteres), Origen (entero
  entre 1 y 5, donde: 1–Argentina, 2–USA, 3–Brasil, 4–Europa, 5–Otro), Género de música de
   la banda (entero entre 1 y 10, donde: 1–Pop, 2–Hard Rock, 3–Soft Rock, 4–Electronic,
    5–Punk, 6–Rap, 7-Progressive, 8-Soul, 9-Reggae, 10-Hip Hop), Escenario donde actuará
     la banda/cantante (cadena de la forma "Flow", "Samsung", "Alternative", "Perry's",
      "Kidzapalooza"), y Cantidad de espectadores prevista para esa banda (un número entero). 
En base a lo anterior, se provee ya desarrollado:
	Un módulo clase.py que contiene la definición de la clase Banda con el
 método constructor y el método __str__() ya incluidos. NO CAMBIE NADA. NO 
 AGREGUE NADA. DEJE LA CLASE TAL CUAL ESTÁ.
	Un segundo módulo principal.py que contiene una función main() con el esquema 
del menú de opciones ya desarrollado y funcionando, de forma que esa función main() 
sea usada como la función de entrada del pro-grama completo y una función de validación
 de carga. En el mismo módulo, se provee ya desarrollada una función generar_aleatorio() 
 que crea con valores aleatorios un objeto de la clase Banda y lo retorna ya listo para usar.
  Los procesos para cumplir con cada opción del menú, son justamente la tarea que debe
   programar cada estudiante. Las opciones a programar son:
1.	Cargar un arreglo de registros con los datos de n bandas (cargar n por teclado y 
validar que sea positivo), de manera que en todo momento el arreglo se mantenga ordenado 
de menor a mayor según el nombre de las bandas. Para esto debe utilizar el algoritmo de 
inserción ordenada con búsqueda binaria (se consi-derará directamente incorrecta la 
solución basada en cargar el arreglo completo y ordenarlo al final, o aplicar el algoritmo
 de inserción ordenada, pero con búsqueda secuencial). La carga de los puestos debe ser
  automática y con base aleatoria (use la función generar_aleatorio() que ya tiene
   disponible en el mó-dulo principal.py para crear los objetos). Cada vez que se 
   ingrese en esta opción, el arreglo debe ser creado desde cero y todo contenido 
   anterior debe ser eliminado.
Ajuste de runner: al ejecutar esta opción, solo cargue por teclado el valor de n,
 y no muestre nada al ter-minar de cargar el vector. Solo regrese al menú.
2.	Mostrar todos los registros del arreglo, a razón de un registro por línea, 
y además, al final del listado mos-trar una línea extra con la suma de la cantidad
 de espectadores esperada entre todas las bandas registra-das. Cuando muestre esta 
 última línea, use ":" para separar el mensaje aclaratorio de salida y el acumula-dor.
Ajuste de runner: al ejecutar esta opción, muestre el listado pedido usando el
 método __str__() que ya tiene en la clase, muestre al final la línea extra con el
  acumulador pedido y regrese al menú (no muestre nada más que eso). 
3.	Buscar si existe una banda cuyo nombre coincide con nom, siendo nom una cadena
 que se carga por te-clado. Si existe, mostrar sus datos. Si además su cantidad de
  espectadores es mayor a 5000, cambiar su escenario (sea cual sea el que tenía) 
  por "Flow", mostrando el registro antes y después de la actualiza-ción. Si l
  a banda no existe, informar con el mensaje: "¡Banda inexistente!".
Ajuste de runner: al ejecutar esta opción, cargue por teclado el valor de nom, muestre el registro (si exis-te) o el mensaje "¡Banda inexistente!" (si no existe), muestre en otra línea el registro actualizado con el nuevo escenario (si corresponde) y regrese al menú (no muestre nada más que eso).
4.	A partir del arreglo, generar un archivo binario donde se incluyan todas las bandas cuyo origen sea USA u Otro, y tengan una cantidad de espectadores mayor que un valor e que se carga por teclado (sin exigen-cia de validación) y que además NO sean del género Reggae.
Ajuste de runner: al ejecutar esta opción, solo genere el archivo pedido y regrese al menú (no muestre nada en la pantalla al terminar).
5.	Mostrar el contenido del archivo binario, a razón de un registro por línea en pantalla, indicando además dos líneas extra: una con la cantidad de bandas mostradas que eran del género Rap o Hip Hop, y otra con la cantidad de bandas que eran de origen Otro. 
Ajuste de runner: al ejecutar esta opción, muestre el listado pedido usando el método __str__() que tie-ne disponible en la clase, muestre al final las dos líneas extra pedidas aquí (use ":" para separar el mensa-je de salida y el valor mostrado en cada una), y regrese al menú (no muestre nada más que eso).
Criterios generales de evaluación.
●	Estructura completa del programa terminado [máximo: 4 puntos por convenciones de estilo, la estructura de las funciones que desarrolle, el control de ejecución del módulo principal, todo otro elemento que aporte a la estructura del programa]
●	Desarrollo correcto del ítem 1: [máximo: 4 puntos]
●	Desarrollo correcto del ítem 2: [máximo: 4 puntos]
●	Desarrollo correcto del ítem 3: [máximo: 4 puntos]
●	Desarrollo correcto del ítem 4: [máximo: 4 puntos]
●	Desarrollo correcto del ítem 5: [máximo: 4 puntos]
●	Para aprobar el parcial (con nota mínima de 4(cuatro), el alumno debe llegar a un porcentaje de al menos 55% del puntaje máximo (eso es, un poco más de 13 puntos).

"""

"""
1.	Cargar un arreglo de registros con los datos de n bandas (cargar n por teclado y 
validar que sea positivo), de manera que en todo momento el arreglo se mantenga ordenado 
de menor a mayor según el nombre de las bandas. Para esto debe utilizar el algoritmo de 
inserción ordenada con búsqueda binaria (se consi-derará directamente incorrecta la 
solución basada en cargar el arreglo completo y ordenarlo al final, o aplicar el algoritmo
 de inserción ordenada, pero con búsqueda secuencial). La carga de los puestos debe ser
  automática y con base aleatoria (use la función generar_aleatorio() que ya tiene
   disponible en el mó-dulo principal.py para crear los objetos). Cada vez que se 
   ingrese en esta opción, el arreglo debe ser creado desde cero y todo contenido 
   anterior debe ser eliminado.
"""
# Use la stock de importación que prefiera.
# Comente una y descomente la otra, a su gusto.
# import clase
from clase import Banda


# Muestra las opciones, y carga y retorna la que elija el usuario.
def menu():
    print("1. Cargar (con inserción ordenada")
    print("2. Mostrar (de acuerdo a lo requerido")
    print("3. Conteo o Búsqueda (según sea requerido)")
    print("4. Generar archivo binario (de acuerdo a lo requerido")
    print("5. Mostrar archivo binario (de acuerdo a lo requerido")
    print("6. Salir del programa.")
    return int(input("Ingrese la opción: "))


# Carga y retorna un número, validando que sea mayor al valor inf que entra como parámetro.
def validar(inf):
    n = int(input('Valor (mayor a ' + str(inf) + ' por favor): '))
    while n <= inf:
        n = int(input('Error... Se pidio mayor a ' + str(inf) + '... Cargue de nuevo: '))
    return n


def generar_aleatorio():
    NOMBRES = (
        "Lola Young", "Un Poco de Ruido", "Violet Grohl", "Juana Rozas", "Ara Palo",
        "Airbag", "Tini", "Travis Scott", "Charli xcx", "The Killers", "David Guetta",
        "Queens of the Stone Age", "The Neighbourhood", "Rawayana", "Fontaines D.C.",
        "Sombr", "The Prodigy", "Dillom", "Dominic Fike", "RAYE", "Cage the Elephant",
        "Usted Señalemelo", "Leon Bridges", "Boys Noize", "Juan Hansen Live"
    )

    LUGARES = ("Flow", "Samsung", "Alternative", "Perry's", "Kidzapalooza")

    nombre = random.choice(NOMBRES)
    origen = random.randint(1, 5)
    genero = random.randint(1, 10)
    escenario = random.choice(LUGARES)
    cantidad = random.randint(1000, 20000)
    return Banda(nombre, origen, genero, escenario, cantidad)

"""
.	A partir del arreglo, generar un archivo binario donde se incluyan todas las bandas cuyo origen sea USA u
 Otro, y tengan una cantidad de espectadores mayor que un valor e que se carga por teclado (sin exigen-cia de validación)
  y que además NO sean del género Reggae.
Ajuste de runner: al ejecutar esta opción, solo genere el archivo pedido y regrese al menú (no muestre nada en la pantalla 
al terminar).
"""
def binary(v,fd,n):
    m = open(fd,"wb")
    for record in v:
        if record.espectadores > n and record.genero != "Reggae":
            pickle.dump(record,m)
    m.close()




def search(v,nom):
    left = 0
    right = len(v) -1
    pos = -1
    while left <= right:
        mid = (left + right) // 2
        if v[mid].nombre == nom:
            pos = mid
            break
        if nom < v[mid].nombre:
            right = mid - 1
        else:
            left = mid + 1
    return pos

def charge(v,n):
    for i in range(n):
        record = generar_aleatorio()
        order(v,record)

def show(v):
    for record in v:

        print(record)

def order(v,record):
    left = 0
    right = len(v) - 1
    pos = 0
    while left <= right:
        mid = (left + right) // 2
        if v[mid].nombre == mid:
            pos = mid
            break
        if record.nombre < v[mid].nombre:
            right = mid -1
        else:
            left = mid + 1
    if left > right:
        pos = left
    v[pos:pos] = [record]

def main():
    random.seed(13715)
    fd = "archivo.dat"
    v = []
    op = -1
    while op != 6:
        op = menu()
        if op == 1:
            n = validar(0)
            charge(v,n)
            pass

        elif op == 2:
            show(v)

            if v:
                pass
            else:
                print("el vector no fue cargado todavía...")

        elif op == 3:
            nom = input("porfavor, ingrese el nombre de la banda:")
            pos = search(v,nom)
            if pos != - 1:
                print("los datos de la banda son: ",v[pos])
                print("el escenario actual es: ", v[pos].escenario)
                if v[pos].espectadores < 5000:
                    v[pos].escenario = "Flow"
                    print("se actualizo el escenario a: ", v[pos].escenario)
                else:
                    print("¡Banda inexistente")

            if v:
                pass
            else:
                print("El vector no fue cargado todavía...")
                """
                Buscar si existe una banda cuyo nombre coincide con nom, siendo nom una cadena
                 que se carga por te-clado. Si existe, mostrar sus datos. Si además su cantidad de
                  espectadores es mayor a 5000, cambiar su escenario (sea cual sea el que tenía) 
                  por "Flow", mostrando el registro antes y después de la actualiza-ción. Si l
                  a banda no existe, informar con el mensaje: "¡Banda inexistente!".
                """



        elif op == 4:

            if v:
                n = validar(0)
                binary(v,fd,n)


                pass
            else:
                print("El vector no fue cargado todavía...")

                """
            4.	A partir del arreglo, generar un archivo binario donde se incluyan todas las bandas cuyo origen sea USA
             u Otro, y tengan una cantidad de espectadores mayor que un valor e que se carga por teclado (sin exigen-cia
              de validación) y que además NO sean del género Reggae.
            Ajuste de runner: al ejecutar esta opción, solo genere el archivo pedido y regrese al menú (no muestre nada
             en la pantalla al terminar).
        """
        elif op == 5:
            if os.path.exists(fd):
                m = open(fd,"rb")
                record = pickle.load(fd)

                for i in record:
                    print(str(record))

                pass
            else:
                print("El archivo", fd, "no existe...")

        elif op == 6:
            print()
            print("Programa terminado... Hasta la vista baby...")
            print()


if __name__ == "__main__":
    main()
