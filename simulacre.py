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
"""
    Determinar el porcentaje entero que representa la cantidad de números pares generados sobre la cantidad
    total de números procesados. Aclaración: NO se pide el porcentaje redondeado, sino truncado, sin
    decimales. Observación: en el cálculo de este porcentaje, haga primero la multiplicación que corresponda, y
    luego la división.
    """
"""
    if numbers % 2 == 0:
        counter_even = counter_even + 1
        percentage_even = (counter_even * 100) // 17000

print("bigger than 1000 and minor than 15000: ",counter_range)
print("the average of divisibles are: ",average)
print("the minor of odd numbers are: ", minor)
print("counter even: ",counter_even)
print("percentage even: ",percentage_even)


"""
"""
Turno 02:
Desarrolle un programa completo en Python que permita generar una sucesión de 14000 números
enteros aleatorios, usando como semilla del generador al valor 973 (es decir, random.seed(973)). 
Los valores de
cada uno de esos 14000 números deben estar entre 100 y 21100 (incluidos ambos -
DEBE usar random.randint(100, 21100) para generar cada uno de estos números).
A modo de elemento de control, y para que cada estudiante sepa si la secuencia que está generando es 
la correcta,
indicamos aquí cuánto debe valer la suma de todos los números generados con el mecanismo indicado:
✓ Suma de todos los números generados: 149000017
A partir de esa sucesión, el programa debe:
1. Determinar cuántos eran menores o iguales que 11000, cuántos eran mayores que 11000 pero menores
que 17000 y además eran divisibles por 3 y por 8 al mismo tiempo, y cuántos eran mayores o iguales que
17000.
2. Determinar el promedio entero de todos los números generados que sean divisibles por 9 pero que sean
también menores o iguales a 15000. Aclaración: NO se pide el promedio redondeado, sino el promedio
truncado, sin decimales.
3. Determinar el mayor entre todos los números generados cuyo valor esté entre 1000 y 14000 (includos
ambos).
4. Determinar el porcentaje entero que la cantidad de números divisibles por 6 representa sobre la cantidad
total de números. Aclaración: NO se pide el porcentaje redondeado, sino truncado, sin decimales.
Observación: en el cálculo de este porcentaje, haga primero la multiplicación que corresponda, y luego la
división.
"""

""""
import random
random.seed(973)

counter_1 = 0
counter_2 = 0
counter_3 = 0
counter_4 = 0
counter_5 = 0
compare_4 = None
add = 0
average = 0
percentage = 0
sum_check = 0


for i in range(14000):
    numbers = random.randint(100,21100)
    sum_check = sum_check + numbers

    if numbers <= 11000:
        counter_1 = counter_1 + 1

    if 11000 < numbers < 17000 and numbers % 3 == 0 and numbers % 8 == 0:
        counter_2 = counter_2 + 1

    if  numbers >= 17000:
        counter_3 = counter_3 + 1

    if numbers % 9 == 0 and numbers <= 15000:
        counter_5 = counter_5 + 1
        add = add + numbers


        average = add//counter_5

    if 1000 <= numbers <= 14000:
        if compare_4 is None or compare_4 < numbers: #"Si el número nuevo es más grande que mi récord, tengo un nuevo récord".
            compare_4 = numbers

    if numbers % 6 == 0:
        counter_4 = counter_4 + 1
        percentage = (counter_4 * 100)//14000

print("counter 1: ",counter_1)
print("counter 2: ",counter_2)
print("counter 3: ",counter_3)
print("average: ",average)
print("the bigger is: ", compare_4)
print("percentage: ",percentage)
print("sum check should be 149000017 ",sum_check)
"""
"""
Desarrolle un programa completo en Python que permita generar una sucesión de 20000 números enteros aleatorios, usando 
como semilla del generador el numero 49 (es decir random.seed(49)). Los valores de cada uno de esos 20000 números deben 
estar entre 1 y 45000 (incluidos ambos) (DEBE usar random.randint(1, 45000) para generar esos números).

A modo de elemento de control, y para que cada estudiante sepa si la secuencia que está generando es la correcta, 
indicamos aquí cuánto debe valer la suma de todos los números generados con el mecanismo indicado:

Suma de todos los números generados: 451459554
A partir de esa sucesión el programa debe:

Indicar cuantos números eran múltiplos de 5, cuántos eran múltiplos de 7 y cuántos eran múltiplos de 9.
Indicar el mayor entre todos aquellos números cuyo último dígito sea mayor o igual a 5 pero menor o igual a 8.
Indicar cuantos números generados son pares menores a 15000.
Indicar el porcentaje entero que representa el punto anterior sobre el total de números procesados. Aclaración 1: NO
se pide el porcentaje redondeado, sino el porcentaje truncado, sin decimales. Aclaración 2: en el cálculo de este porcen
taje, haga primero la multiplicación que corresponda, y luego la división.
Cuando finalice, en las consignas que siguen en este mismo cuestionario, se le pedirá que informe cada uno de estos resu
ltados, y también se le pedirá que suba el archivo de código fuente con el programa desarrollado (por lo que tenga muy presente en donde dejó ese archivo). Entienda: Si NO sube su código fuente, los profesores procederán a reprobar manualmente su parcial. Habrá también UNA pregunta de opciones múltiples referida a este mismo enunciado o a temas relacionados con él.
"""
"""
import random
random.seed(49)
counter_1 = 0
counter_2 = 0
counter_3 = 0
counter_4 = 0
bigger = None
percentage = 0

for i in range(20000):
    number = random.randint(1, 45000)

    if number % 5 == 0:
        counter_1 = counter_1 + 1
    if number % 7 == 0:
        counter_2 = counter_2 + 1

    if number % 9 == 0:
        counter_3 = counter_3 + 1

    module = number % 10
    if 5 <= module <= 8:
        if bigger is None or bigger < number:
            bigger = number

    if number % 2 == 0 and number > 15000:
        counter_4 = counter_4 + 1

#counter 4 is for even numbers

percentage = (counter_4 * 100) // 20000

print("multiples of 5: ",counter_1)
print("multiples of 7: ",counter_2)
print("multiples of 9: ",counter_3)
print("evens lesser than 15000 ", counter_4)
print("percentage is: ", percentage)
print("bigger is: ", bigger)


"""
"""
Turno 03:
Desarrolle un programa completo en Python que permita generar una sucesión de 19000 números
enteros aleatorios, usando como semilla del generador al valor 3374 (es decir, random.seed(3374)). Los valores de
cada uno de esos 19000 números deben estar entre -1000 y 15000 (incluidos ambos - DEBE usar random.randint(-
1000, 15000) para generar cada uno de estos números).
A modo de elemento de control, y para que cada estudiante sepa si la secuencia que está generando es la correcta,
indicamos aquí cuánto debe valer la suma de todos los números generados con el mecanismo indicado:
✓ Suma de todos los números generados: 133091344
A partir de esa sucesión, el programa debe:
1. Determinar cuántos eran negativos. Además, determinar cuántos eran mayores o iguales a 0 y menores
que 12000 pero además eran divisibles por 5. Y finalmente determinar cuánto es la suma de los que eran
mayores o iguales a 12000 pero además eran divisibles por 3.
2. Determinar el promedio entero de todos los números generados que estén entre -200 y 3000 (incluídos
ambos). Aclaración: NO se pide el promedio redondeado, sino el promedio truncado, sin decimales.
3. Determinar el menor entre todos los números generados que no sean negativos y además sean divisibles
por 9.
4. Determinar el porcentaje entero que la cantidad de números generados pares negativos representa sobre
la cantidad total de números procesados. Aclaración: NO se pide el porcentaje redondeado, sino truncado,
sin decimales. Observación: en el c

"""
"""
import random
random.seed(3374)
control = 0
counter_1 = 0
counter_2 = 0
counter_3 = 0
counter_4 = 0
counter_5 = 0
lesser = None
average = 0
percentage = 0
add = 0

for i in range(19000):
    number = random.randint(-1000,15000)
    control = control + number

    if 0 > number:
        counter_1 = counter_1 + 1


    if 0 <= number < 12000 and number % 5 == 0:
        counter_2 = counter_2 + 1

    if 12000 <= number and number % 3 == 0:
        add = add + number

    if -200 <= number <= 3000:
        counter_3 = counter_3 + number
        counter_5 = counter_5 + 1

        average = counter_3//counter_5


    if 0 <= number and number % 9 == 0:

        if lesser is None or  lesser > number:
            lesser = number

    if 0 > number and number % 2 == 0:
        counter_4 = counter_4 + 1

        percentage = (counter_4 * 100) // 19000

print("plus 0: ",counter_1)
print("plus 0, minus 12000 and % 5: ",counter_2)
print("the addition is: ", add)
print("the average is: ", average)
print("the percentage of even negatives are: ", percentage)
print("the lesser is: ", lesser)
"""
"""
Turno 04:
Desarrolle un programa completo en Python que permita generar una sucesión de 25000 números
enteros aleatorios, usando como semilla del generador al valor 7658 (es decir, random.seed(7658)).
 Los valores de
cada uno de esos 25000 números deben estar entre -2500 y 45000 (incluidos ambos - DEBE usar random.randint(-
2500, 45000) para generar cada uno de estos números).
A modo de elemento de control, y para que cada estudiante sepa si la secuencia que está generando es la
 correcta,
indicamos aquí cuánto debe valer la suma de todos los números generados con el mecanismo indicado:
✓ Suma de todos los números generados: 529572772
A partir de esa sucesión, el programa debe:
1. Determinar cuántos eran menores o iguales que -500; cuántos eran mayores que -500 y menores que
27000, y cuántos eran mayores o iguales que 27000 pero además eran divisibles por 10.
2. Determinar el promedio entero entre los números mayores a 0 y divisibles por 7 o por 8. Aclaración: 

pide el promedio redondeado, sino truncado, sin decimales.
3. Determinar el mayor entre todos los números generados que sean negativos divisibles por 4.
4. Determinar el porcentaje entero que la cantidad de números menores que 5000 representa sobre la
cantidad total de números. Aclaración: NO se pide el porcentaje redondeado, sino truncado, sin decimales.
Observación: en el cálculo de este porcentaje, haga primero la multiplicación que corresponda, y luego la
división.
"""
"""
import random
random.seed(7658)
check = 0
counter_1 = 0
counter_2 = 0
counter_3 = 0
counter_4 = 0
counter_5 = 0
add = 0
average = 0
bigger = None
percentage = 0
for i in range(25000):
    number = random.randint(-2500,45000)
    check = check + number

    if -500 >= number:
        counter_1 = counter_1 + 1

    if -500 < number < 27000:
        counter_2 = counter_2 + 1

    if 27000 >= number and number % 10 == 0:
        counter_3 = counter_3 + 1

    if 0 < number:
        add = add + number

    if number % 7 == 0 or number % 8 == 0:
        counter_4 = counter_4 + 1

    average = add // counter_4

    if 0 > number and number % 4 == 0:
        if bigger is None or bigger < number:
            bigger = number

    if 5000 > number:
        counter_5 = counter_5 + 1
        percentage = (counter_5 * 100) // 25000

"""

"""
print("the number should be: 529572772", check)
print("-500 are: ",counter_1)
print("-500 and < 27000 are: ",counter_2)
print("> 27000 and % 10 are: ",counter_3)
print("average is: ",average)
print("percentage is: ",percentage)
print("bigger is: ",bigger)

"""

"""
Desarrolle un programa completo en Python que permita generar una sucesión de 25000 números enteros aleatorios, 
usando como semilla del generador el número 20220512 (es decir random.seed(20220512)). Los valores de cada uno
 de esos 25000 números deben estar entre 1 y 45000 (incluidos ambos) (DEBE usar random.randint(1, 45000) para
  generar esos números). A partir de esa sucesión el programa debe:

Determinar la cantidad de números múltiplos de 3 y también la cantidad de números múltiplos de 5 pero no de 3 y
 finalmente la cantidad de números que no cumplen ninguna de las 2 condiciones.
Indicar el mayor entre todos los números comienzan con el dígito 1, es decir 1234 comienza con 1 y 2345 no
 comienza 
con 1.
Indicar el promedio entero truncado de los números generados que son pares y múltiplos de 11.
Indicar el porcentaje entero que representa cada contador del punto 1. Aclaración 1: NO se pide el porcentaje redondeado
, sino el porcentaje truncado, sin decimales. Aclaración 2: en el cálculo de este porcentaje, haga primero la multip
licación que corresponda, y luego la división.
Cuando finalice, en las consignas que siguen en este mismo cuestionario, se le pedirá que informe cada uno de estos res
ultados, y también se le pedirá que suba el archivo de código fuente con el programa desarrollado (por lo que tenga muy
 presente en donde dejó ese archivo). Habrá también UNA pregunta de opciones múltiples referida a este mismo enunciado 
o a temas relacionados con él.
"""
"""
import random
random.seed(20220512)
counter_0 = 0
counter_1 = 0
counter_2 = 0
counter_3 = 0
add = None
average = 0
add_1 = 0

for i in range(25000):
    number = random.randint(1,45000)

    if number % 3 == 0:
        counter_0 = counter_0 + 1

    if number % 5 == 0 and number % 3 != 0:
        counter_1 = counter_1 + 1

    if number % 5 != 0 and number % 3 == 0:
        counter_2 = counter_2 + 1

    if str(number) [0] == "1":
        if add is None or add < number:
            add = number


    if number % 2 == 0 and number % 11 == 0:
        counter_3 = counter_3 + 1
        add_1 = add_1 + number


        average = add_1 // counter_3

percentage_0 = (counter_0 * 100) // 25000
percentage_1 = (counter_1 * 100) // 25000
percentage_2 = (counter_2 * 100) // 25000
print("3 multiples: ", counter_0)
print("5 multiples ,3 dosent: ",counter_1)
print("opossite conditions: ",counter_2)
print("the bigger is: ",add)
print("average is: ", average)
print("percentage 1 ",percentage_0)
print("percentage 2 ",percentage_1)
print("percentage 3 ",percentage_2)
"""
"""
urno 01:
Desarrolle un programa completo en Python que permita generar una sucesión de 15000 números
enteros aleatorios, usando como semilla del generador al valor 2759 (es decir, random.seed(2759)). 
Los valores de
cada uno de esos 15000 números deben estar entre 1 y 53000 (incluidos ambos - DEBE usar random.randint(1,
53000) para generar cada uno de estos números). En la última pregunta de este cuestionario, se le pedirá 
que suba
el archivo de código fuente: Subir el archivo de código fuente es OBLIGATORIO: no subirlo, equivale a un 
aplazo
directo, sin importar lo que sea que haya respondido en las preguntas previas de esta evaluación.
A modo de elemento de control, y para que cada estudiante sepa si la secuencia que está generando es la correcta,
indicamos aquí cuánto debe valer la suma de todos los números generados con el mecanismo indicado:
✓ Suma de todos los números generados: 398386184
A partir de esa sucesión, el programa debe:
1.    1. Determinar cuántos de esos números eran mayores o iguales a 1 pero menores que 17000, cuántos eran
mayores o iguales que 17000 pero menores que 37000, y cuántos eran mayores o iguales que 37000
2. Determinar el promedio entero de los números generados que eran mayores o iguales que 25000 pero a su
vez divisibles por 4. Aclaración: NO se pide el promedio redondeado, sino truncado, sin decimales.
3. Determinar el mayor entre todos los números generados que sean divisibles por 3.
4. Determinar el porcentaje entero que representa la cantidad de números divisibles por 5 generados sobre la
cantidad total de números procesados. Aclaración: NO se pide el porcentaje redondeado, sino truncado,
sin decimales. Observación: en el cálculo de este porcentaje, haga primero la multiplicación que
corresponda, y luego la división.
"""
"""
import random
random.seed(2759)
check = 0
counter_1 = 0
counter_2 = 0
counter_3 = 0
counter_4 = 0
counter_5 = 0
average = 0
percentage = 0
add = 0
bigger = 0

for i in range(15000):

    number = random.randint(1,53000)

    if 1 <= number < 17000:
        counter_1 = counter_1 + 1
    if 17000 <= number  < 37000:
        counter_2 = counter_2 + 1
    if 37000 <= number:
        counter_3 = counter_3 + 1

    if 25000 <= number and number % 4 == 0:
        add = add + number
        counter_4 = counter_4 + 1

        average = add // counter_4

       
    if number % 3 == 0:
        if bigger is None or bigger < number:
            bigger = number

    if number % 5 == 0:
        counter_5 = counter_5 + 1

        percentage = (counter_5 * 100) // 15000



print("more than 1 less than 17000: ", counter_1)
print("more tan 17000 less than 37000: ",counter_2)
print("moore than 37000L ", counter_3)
print("the average is ", average)
print("the bigger is ", bigger)
print("the percentage is ",percentage)

"""

"""
Turno 02:
Desarrolle un programa completo en Python que permita generar una sucesión de 18000 números
enteros aleatorios, usando como semilla del generador al valor 7633 (es decir, random.seed(7633)).
 Los valores de
cada uno de esos 18000 números deben estar entre 500 y 13500 (incluidos ambos -
DEBE usar random.randint(500, 13500) para generar cada uno de estos números). En la última pregunta de este
cuestionario, se le pedirá que suba el archivo de código fuente: Subir el archivo de código fuente es
OBLIGATORIO: no subirlo, equivale a un aplazo directo, sin importar lo que sea que haya respondido en las
preguntas previas de esta evaluación.
A modo de elemento de control, y para que cada estudiante sepa si la secuencia que está generando es la correcta,
indicamos aquí cuánto debe valer la suma de todos los números generados con el mecanismo indicado:
✓ Suma de todos los números generados: 125167944

. Determinar cuántos eran menores o iguales que 4000, cuántos eran mayores que 4000 pero menores que
10000 y además eran divisibles por 4, y cuántos eran mayores o iguales que 10000.
2. Determinar el promedio entero de todos los números generados que sean pares y divisibles por 6.
Aclaración: NO se pide el promedio redondeado, sino el promedio truncado, sin decimales.
3. Determinar el menor entre todos los números generados cuyo valor sea menor o igual a 12000.
4. Determinar el porcentaje entero que la cantidad de números divisibles por 8 representa sobre la cantidad
total de números. Aclaración: NO se pide el porcentaje redondeado, sino truncado, sin decimales.
Observación: en el cálculo de este porcentaje, haga primero la multiplicación que corresponda, y luego la
división.


"""

import random
random.seed(7633)
check = 0
counter_1 = 0
counter_2 = 0
counter_3 = 0
add = 0
counter_4 = 0
counter_5 = 0
minor = None
average = 0
percentage = 0

for i in range(18000):
    number = random.randint(500,13500)

    if 4000 >= number:
        counter_1 = counter_1 + 1

    elif 4000 < number < 10000 and number % 4 == 0:
        counter_2 = counter_2 + 1

    else:
        counter_3 = counter_3 + 1

    #2. Determinar el promedio entero de todos los números generados que sean pares y divisibles por 6.
    if number % 2  == 0 and number % 6 == 0:
        add = add + number
        counter_4 = counter_4 + 1
        average = add // counter_4

    #3 Determinar el menor entre todos los números generados cuyo valor sea menor o igual a 12000.

    if 12000 >= number:
        if minor is None or minor > number:
            minor = number

    #4 4. Determinar el porcentaje entero que la cantidad de números divisibles por 8 representa sobre la cantidad

    if number % 8 == 0:
        counter_5 = counter_5 + 1
        percentage = (counter_5 * 100) // 18000

print("4000>n" , counter_1)
print("4000 < number < 10000 number % 4", counter_2)
print(">10000 ", counter_3)
print("average", average)
print("minor", minor)
print("percentage", percentage)

























