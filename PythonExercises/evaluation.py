"""
Turno 1
Consignas Generales.
Enunciado:
 Por cada Empleo se tienen los siguientes datos: el número de identificación del empleo, la descripción
del empleo, el tipo de empleo (un valor del 0 al 39) y el monto mensual del sueldo o retribución que se paga por
ese empleo. Se desea almacenar la información referida a los n empleos en un arreglo de objetos de tipo Empleo
(definir la clase Empleo y cargar n por teclado, validando que sea mayor a cero). Se pide desarrollar un programa
en Python controlado por un menú de opciones, que permita gestionar las siguientes tareas:
1. Cargar el arreglo pedido con los datos de los n empleos. Valide o asegure que los valores de cada campo sean
correctos.
2. Mostrar todos los datos de todos los empleos, a razón de uno por línea, en un listado ordenado de menor a
mayor según la descripción de los empleos. Al final del listado indique la suma de los sueldos a pagar por todos
los empleos que se mostraron.
3. Determinar la cantidad de empleos que hay en el arreglo por cada tipo de empleo posible (40 contadores en
total en un vector de conteo). Muestre solo los valores de los contadores cuyos valores finales sean mayores a
cero.
4. Determinar si existe un empleo cuyo número de identificación sea igual num, siendo num un valor que se carga
por teclado. Si existe, mostrar solo su descripción y el sueldo a pagar. Si no existe, informar con un mensaje. Si
existe más de un registro que coincida con esos parámetros de búsqueda, debe mostrar sólo el primero que
encuentre. La búsqueda debe detenerse al encontrar el prime objeto que coincida con el criterio pedido.


"""
import random
import clase




#validacion de inf que entr como parametro
def validate(inf):
    number = int(input("valor(mayor a " + str(inf) + "porfa"))
    while number <= inf:
        number = int(input("error , se pidio mayor a" + str(inf) + "carge de nuevo"))
    return number




#crear y poblar el vector de empleos mediante generación aleatoria de datos de prueba.
def charge():
    number = validate(0)
    v = number * [None]
    names = ("Oficinista", "Mecanico", "Jardinero", "Programador", "Maestro")
    for i in range(number): # Genera y asigna de forma aleatoria cada atributo para los $n$ elementos
        id = random.randint(1,25000) #identificador unico
        de = random.choice(names) + " " + str(i) # Toma una profesión al azar y le concatena el índice $i$ para garantizar descripciones variadas e independientes.
        ti = random.randint(0,39) #Genera el tipo de empleo entre 0 y 39 (40 tipos posibles), clave para el conteo por frecuencias del ítem 3.
        im = round(random.uniform(0,2000),2)
        v[i] = clase.Empleo(id, de, ti, im) #crea un objeto, ejecuta su constructor y guarda su referencia en una posición específica del vector.
    print("succes")
    return v







def show(v):
    number = len(v)
    #seleccion directa
    for i in range(number - 1):
        for j in range(i+1, number):
            if v[i].descripcion > v[j].descripcion:
                v[i], v[j] = v[j], v[i]
    print("listadpo de empleos")
    ac = 0 # Inicializa una variable acumuladora en cero antes de entrar al bucle para sumar los sueldos.
    for i in range(number):
        ac += v[i].importe
        print(v[i])
    print("suma de todos los sueldos pagados", ac)
    print()

def count(v):
    number = len(v) #: Calcula el tamaño del arreglo para saber cuántos objetos Empleo debemos recorrer.
    c = 40 * [0] #Inicialización del vector de conteo. Crea una lista de exactamente 40 casilleros
    #Los índices válidos para acceder a esta lista van del 0 al 39, coincidiendo exactamente con el rango posible de tipos de empleo.
    for i in range(number):
        #ind = v[i].tipo
        # c[ind] += 1
        c[v[i].tipo] += 1


        """
        v[i].tipo: Consulta el atributo .tipo del objeto actual (que guarda un número entero entre 0 y 39).

c[v[i].tipo] += 1: Utiliza ese número como el índice del vector c para incrementar su casillero en 1.
        """

    print("empleos por tipo ")
    for k in range(40):
        if c[k] !=0:
            print("tipo:", k, "cantidad:", c[k])
    print()


def buscar(v):
    n = len(v)
    num = int(input("Número de identificación del empleo a buscar: "))
    for i in range(n):
        if num == v[i].identificador:
            print("Encontrado:")
            print(
                "Descripción del empleo:",
                v[i].descripcion,
                " - Sueldo:",
                v[i].importe,
            )
            print()
            return
    print("No estaba...")
    print()


"""
Explicación paso a paso1. Obtención del tamaño y carga del valor a buscar:n = len(v): Calcula la cantidad de objetos en
 el vector para limitar el rango del ciclo.num = int(input(...)): Solicita por teclado el ID del empleo que el usuario 
 desea encontrar.2. Algoritmo de Búsqueda Secuencial con Interrupción Temprana:for i in range(n):: Recorre los elementos
  del vector posición por posición, de izquierda a derecha.if num == v[i].identificador::Compara el valor num ingresado
   contra la propiedad .identificador del objeto guardado en v[i].print(...):Si hay coincidencia, imprime exclusivamente
   la descripción (v[i].descripcion) y el sueldo (v[i].importe), tal como lo exige el enunciado.return:Interrupción 
   inmediata de la función. Al ejecutar return, la función termina al instante y vuelve al menú principal. Esto 
   garantiza que no siga recorriendo el resto del vector inútilmente una vez que encontró la primera coincidencia
    (requisito explícito del parcial).3. Manejo de Búsqueda Sin Éxito:print("No estaba..."):Esta línea está fuera 
    del ciclo for. Solo se ejecutará si el ciclo terminó todas sus iteraciones ($0$ a $n-1$) sin que la instrucción
     return haya cortado la función, indicando que el ID no existía en el arreglo.
"""



def principal():
    v = []
    option = -1
    while option != 5:
        print("1. Charge array")
        print("2. Show order ")
        print("3. Count by type")
        print("4. Search")
        print("5. Exit")
        option = int(input("type a option number"))

        if option == 1:
            v = charge()
        elif option == 2:
            if v:
                show(v)
            else:
                print("the vector was not charged yet")
        elif option == 3:
            if v:
                count(v)
            else:
                print("the vector was not charged yet")
        elif option == 4:
            if v:
                search(v)
            else:
                print("el vector no fue cargado todavía...")
        elif option == 5:
            print("Programa terminado... Hasta la vista baby...")

if __name__ == "__main__":
    principal()
