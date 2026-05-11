"""
. Ciclistas
La final de una carrera de ciclistas tiene n competidores (n se ingresa por teclado).
Desarrollar un programa que permita cargar, por cada competidor, nombre y tiempo de carrera. Luego se pide:
a) Determinar y mostrar el nombre del ganador de la carrera.
b) Ingresar por teclado el tiempo record registrado para dicha carrera. Determinar si el tiempo del ganador es menor
al tiempo record, mostrar un mensaje.
c) Calcular y mostrar el tiempo promedio entre todos los ciclistas.
"""
#if mayor is None or mayor < monto_mensual
"""
racers_number = int(input("racers numbers: "))
name_count = ""
time_count = 0
best_time = None

for i in range(racers_number):

    names = input("input the name: ")
    times = int(input("input the time: "))
    time_count = time_count + times

    if best_time is None or times < best_time:
        best_time = times
        name_count = names
 
print("the winner is: ", name_count)

average = time_count/racers_number

record = int(input("the record is: "))
if record > best_time:
    print("the best time surpasses the record: ", best_time)
    print("the average is: ", average)
else:
    print("the record was not surpassed: ", record)
    print("the average is: ", average)
"""

"""
Secuencia de impares
Cargar por teclado dos números, e imprimir los 
números impares que se encuentran comprendidos entre ellos, en forma ascendente y descendente.
"""

number_one = int(input("input first number: "))
number_two = int(input("input second number: "))


if number_one < number_two and number_one % 2 == 0:

    for i in range(number_one -1, number_two + 1,2):
        print(i)

    for i in range(number_two-1,number_one -2,-2):
        print(i)
else:
    for i in range(number_one,number_two+1,2):
        print(i)

    for i in range(number_two -1 , number_one + 2, -2):
        print(i)


































