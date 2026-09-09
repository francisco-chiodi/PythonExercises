"""
Un compañía aérea necesita un programa para gestionar la información de los tickets que tiene ya vendidos.
 Por cada ticket se conoce:
el código del vuelo (una cadena) -> LA HACES VOS ES UNA TUPLA

 número de identificación del pasajero que compró el ticket -> random.randint(0 , 400)  HACELO CON RANDOMRANDINT NO HAY LIMITE FIJADO

 el país de destino del vuelo (un valor entre 1 y 20) ACA RANDOMRANDINT SI TIENE LIMITE FIJADO

el número de asiento asignado -> NO HAY LIMITE FIJA ALGO RAZONABLE CON RANDOMRANDINT SI ES UN AVION SON 200 ASIENTOS

y el importe pagado por ese ticket. -> FIJA ALGO RAZONABLE

Se desea almacenar la información referida a los n tickets en un arreglo de objetos de tipo Ticket
(definir el tipo Ticket y cargar n por teclado). Se pide desarrollar un programa en Python controlado por un menú
de opciones y que posea como mínimo dos módulos, que permita gestionar las siguientes tareas:

a. Cargar el arreglo con los datos de los n tickets. Valide o asegure que los datos cargados sean correctos. Puede
hacer la carga en forma manual, o puede generar los datos en forma automática.

b. Mostrar los datos de todos los tickets cuyo número de asiento sea mayor a un valor num que se carga por
teclado, ordenados por código de vuelo de menor a mayor. Los tickets se deben mostrar a razón de uno por
línea (no más de una línea por ticket en la pantalla).

c. Determine el importe acumulado que se cobró por cada posible país de destino (20 acumuladores en un vector
de acumulación). Muestre solo aquellos acumuladores cuyo valor sea mayor un valor t que se carga por
teclado.

d. Determinar si existe un ticket cuyo número de identificación del pasajero sea igual a id. Si se encuentra,
mostrar el número de asiento y el país de destino. Si no se encuentra, indicar con un mensaje que no existe.
Debe mostrar los datos del primero que encuentre y detener en ese momento la búsqueda (sin importar si hay
más de un registro con el mismo código).

"""
import clase_2
import random

def validate(inf):
    number = int(input("ingrese un numero mayor a "+ str(inf) + " porfavor"))
    while number <= inf:
        number = int(input("error. ingrese un numero del 1 al 5"))
    return number


def charge():
    number = validate(0)
    v = number * [None]
    names = ("AJ","AA","AE","MN","LS","HL","UB","CS","PE")#codigo de vuelo
    for i in range(number):#genera y asigna aleatoreamente cada atributo a los elementos
        flycode = random.choice(names) + str(i)
        """FIJATE QUE EL STR(I) EVITA QUE SE DUPLIQUEN NOMBRES ,
         CADA UNO ES UNICO POR EL INDICE AUNQUE SOLO SEAN 9.
         EL PUNTO 2 PIDE ORDNAR , TAMBIEN SIRVE PARA ESO"""
        passager_id = random.randint(1,400)
        destination = random.randint(1,20)
        seat_number = random.randint(1,200)
        total =  round(random.uniform(0,20000),2)
        v[i]= clase_2.Ticket(flycode,passager_id,destination,seat_number,total)
        print("el arreglo fue generado")
        print()
    return v

"""
b. Mostrar los datos de todos los tickets cuyo número de asiento sea mayor a un valor num que se carga por
teclado, ordenados por código de vuelo de menor a mayor. Los tickets se deben mostrar a razón de uno por
línea (no más de una línea por ticket en la pantalla).
"""

def show(v): #seleccion directa

    number = len(v)

    for i in range(number-1): #el ultimo no se considera porque ya estara ordenado al finalizar el ciclo
        for j in range(i+1,number): #no se cuenta el primero para encontrar menores a su derecha y remplazar
            if v[i].flycode > v[j].flycode:
                v[i],v[j] = v[j], v[i]
        """
        2. Filtrado e Impresión: Le pide al usuario un entero num.
        Recorre el arreglo ya ordenado posición por posición.
        Con la condición if v[i].seat_number > num, evalúa si el asiento del ticket actual supera el número ingresado.
        Si cumple la condición, ejecuta print(v[i]),
        lo cual llama automáticamente al método __str__ del ticket para mostrarlo en pantalla.
        """
        num = int(input("sit number (se mostraran los asientos con numeros mayores a :"))
        print("listado de tickets con numero de asiento mayor a",num,":")
        for i in range(number):
            if v[i].seat_number > num:
                print(v[i])
        print()


    """
    c. Determine el importe acumulado que se cobró por cada posible país de destino (20 acumuladores en un vector
    de acumulación). Muestre solo aquellos acumuladores cuyo valor sea mayor un valor t que se carga por
    teclado.
    """
def accumulator(v):
        number = len(v)
        c = 20 * [0]

        for i in range(number):
            # el número de pais viene entre 1 y 20... restar uno para compatibilizar con los índices del vector c...
            indice = v[i].pais - 1
            """Miramos el objeto: v[0].destination vale 3 (País 3).
            Se ejecuta la línea: indice = v[0].destination Matematicamente: ind = 3 - 1
            Resultado: La variable indice ahora vale 2.
            Inmediatamente después se ejecuta: c[indice] += v[0].total
            Python reemplaza la variable indice por su valor numérico actual (2).
            La instrucción se convierte internamente en: c[2] += v[0].total
            Va a la posición 2 del vector c (que representa al País 3) y le suma el dinero de ese ticket.
            indice es solo una "caja temporal" donde guardas el número de casillero que calculaste antes de ir a modificar la lista c."""
            c[indice] += v[i].total
        t = int(input("Importe (se mostrarán los acumuladores mayores a este valor):"))
        print("Importes acumulados por país, mayores a", t, ":")

        for k in range(20):
            if c[k] > t:
                print("Pais destino:", k + 1, "Importe acumulado:", round(c[k], 2))

                # si al contar/acumular resté uno, entonces en pantalla, y SOLO EN PANTALLA, mostrar k+1...



"""
d. Determinar si existe un ticket cuyo número de identificación del pasajero sea igual a id. Si se encuentra,
mostrar el número de asiento y el país de destino. Si no se encuentra, indicar con un mensaje que no existe.
Debe mostrar los datos del primero que encuentre y detener en ese momento la búsqueda (sin importar si hay
más de un registro con el mismo código).
"""

def search(v):
    number = len(v)
    passeger_id = int(input("passeger number"))
    for i in range(number):
        if passeger_id == v[i].passeger_id:
            print("found:")
            print("seat: ", v[i].seat_number, "destination", v[i].destination)
            return #una instrucción return sin ningún valor cumple la función de interrumpir y salir de la función de manera inmediata.
    print("didnt found")
    print()


def principal():
    v = []
    option = -1
    while option != 5:
        print("1. Cargar arreglo")
        print("2. Mostrar arreglo")
        print("3. Acumular por pais")
        print("4. Buscar")
        print("5. Salir")

        option = int(input("ingrese numero de opcion: "))
        if option == 1:
            v = charge()
        elif option == 2:
            if v:
                v = show(v)
            else:
                print("el vector no fue cargado todavia: ")
                print()
        elif option == 3:
            if v:
                accumulator(v)
            else:
                print("el vector no fue cargado todavia: ")
                print()
        elif option == 4:
            if v:
                search(v)
            else:
                print("el vector no fue cargado todavia: ")
                print()
        elif option == 5:
            print("Programa terminado... Hasta la vista baby...")
            print()

if __name__ == "__main__":
    principal()