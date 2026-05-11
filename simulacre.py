"""generar sucesion de 20000 numeros aleatorios
usando la semilla generador numero 49 random.seed(49)
con valores entre 1 y 45000
random.randint(1,45000) para generar los numeros.
la suma de todos los numeros generados es 451459554

indicar cuantos son multiplos de 5 , cunatos multiplos de 7 y cuantos
multiplos de 9

indicar el mayor de ellos cuyo ultimo digito sea mayor o igual a 5 pero menor o igual a 8
"""
import random
random.seed(49)
multiples = None
number_check = 0

for i in range(0,20000):
    numbers = random.randint(1, 45000)

    if i % 315 == 0:
     print("5,7 and 9 multples: ", i)
#modulo de 10










