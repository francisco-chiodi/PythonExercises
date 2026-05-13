"""generar sucesion de 20000 numeros aleatorios
usando la semilla generador numero 49 random.seed(49)
con valores entre 1 y 45000
random.randint(1,45000) para generar los numeros.
la suma de todos los numeros generados es 451459554

indicar cuantos son multiplos de 5 , cunatos multiplos de 7 y cuantos
multiplos de 9

indicar el mayor de ellos cuyo ultimo digito sea mayor o igual a 5 pero menor o igual a 8

indicar cuantos son pares menores a 15000



"""

"""
import random
random.seed(49)
five_eight = None
counter_pair = 0

for i in range(0,20000):
    numbers = random.randint(1, 45000)

    if numbers % 315 == 0:
        print("5,7 and 9 multples: ", numbers)

    if numbers % 10 in (5,6,7,8):

        if five_eight is None or numbers > five_eight:
            five_eight = numbers

    if numbers % 2 == 0 and numbers <= 15000:
        counter_pair = counter_pair + 1



print("five eight bigger: ", five_eight)
print("are pairs lesser than 15000: ", counter_pair)

"""



#modulo de 10
"""
Desarrolle un programa completo en Python que permita generar una sucesión de 17000 números
enteros aleatorios, usando como semilla del generador al valor 1157 (es decir, random.seed(1157)). 
Los valores de
cada uno de esos 17000 números deben estar entre 1000 y 37000 (incluidos ambos -
DEBE usar random.randint(1000, 37000) para generar cada uno de estos números).
"""
import random
compare = None
minor = None
random.seed(1157)
#322152298
divisible = 0
counter = 0
average = 0
ave_sum = 0
counter_even = 0
divisible_even = 0
counter_range = 0
average_even = 0
percentage_even = 0
#Determinar cuántos de esos números eran mayores o iguales a 1000 pero menores que 15000
for i in range(17000):
    numbers = random.randint(1000,37000)
    if 1000 < numbers < 15000:
        counter_range = counter_range + 1

#Determinar el promedio entero de los números generados que eran divisibles por 7 pero no por 3.

    if numbers % 7 == 0 and numbers % 3 != 0:
        ave_sum = ave_sum + numbers
        counter = counter + 1
        average = ave_sum // counter


#3. Determinar el menor entre todos los números generados que sean impares.

    if numbers % 2 != 0:
        if minor is None or numbers < minor:
            minor = numbers
    """
    Determinar el porcentaje entero que representa la cantidad de números pares generados sobre la cantidad
    total de números procesados. Aclaración: NO se pide el porcentaje redondeado, sino truncado, sin
    decimales. Observación: en el cálculo de este porcentaje, haga primero la multiplicación que corresponda, y
    luego la división.
    """
    if numbers % 2 == 0:
        counter_even = counter_even + 1
        percentage_even = (counter_even * 100) // 17000

print("bigger than 1000 and minor than 15000: ",counter_range)
print("the average of divisibles are: ",average)
print("the minor of odd numbers are: ", minor)
print("counter even: ",counter_even)
print("percentage even: ",percentage_even)




















