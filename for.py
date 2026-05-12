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
"""
"""
3. Sueldos y aguinaldo
Ingresar por teclado los sueldos de un vendedor, correspondientes al primer semestre del año y luego:

a) Calcular su aguinaldo, sabiendo que es la mitad del sueldo más alto del período.

b) Determinar en qué mes recibió el sueldo más bajo del período.

c) Informar el sueldo promedio del semestre.

"""
months = 6
salary_accumulator = 0
best_salary = None
less_salary = None
name_count = ""
name = ""
name_1 = ""
boost = 0
average = None

for i in range(months):
    if i == 0:
        january_salary = int(input("january salary is: "))
        salary_accumulator = salary_accumulator + january_salary

        if best_salary is None or january_salary > best_salary:
            best_salary = january_salary
            name_1 = "january"

        if best_salary is None or january_salary < best_salary:
            less_salary = january_salary
            name = "january"


    elif i == 1:
        february_salary = int(input("february salary is: "))
        salary_accumulator = salary_accumulator + february_salary

        if best_salary is None or february_salary > best_salary:
            best_salary = february_salary
            name_1 = "february"


        if less_salary is None or february_salary < less_salary:
            less_salary = february_salary
            name = "february"


    elif i == 2:
        march_salary = int(input("march salary is: "))
        salary_accumulator = salary_accumulator + march_salary

        if best_salary is None or march_salary > best_salary:
            best_salary = march_salary
            name_1 = "march"

        if less_salary is None or march_salary < less_salary:
            less_salary = march_salary
            name = "march"

    elif i == 3:
        april_salary = int(input("aplil salary is: "))
        salary_accumulator = salary_accumulator + april_salary

        if best_salary is None or april_salary > best_salary:
            best_salary = april_salary
            name_1 = "april"

        if less_salary is None or april_salary < less_salary:
            less_salary = april_salary
            name = "april"


    elif i == 4:
        may_salary = int(input("may salary is: "))
        salary_accumulator = salary_accumulator + may_salary

        if best_salary is None or may_salary > best_salary:
            best_salary = may_salary
            name_1 = "may"

        if less_salary is None or may_salary < less_salary:
            less_salary = may_salary
            name = "may"

    elif i == 5:
        june_salary = int(input("june salary is: "))
        salary_accumulator = salary_accumulator + june_salary

        if best_salary is None or june_salary > best_salary:
            best_salary = june_salary
            name_1 = "june"

        if less_salary is None or june_salary < less_salary:
            less_salary = june_salary
            name = "june"


    boost = best_salary / 2
    average = salary_accumulator / months


print("the salary is: ",salary_accumulator)
print("best salary is: ", best_salary, "on the month: ",name_1)
print("aguinaldo: ",boost)
print("lesser salary was: ", less_salary , "on the month: ",name )
print("the average salairi is: ", average)


































