"""
Desarrolle un programa que permita genera una sucesion de 20000 numeros enteros aleateorios
la semilla del generador es el numero 49, random.seed(49)
Los valores de los 20000 numeros deben estar entre 1 y 45000 ambos incluios
Usar random.randint(1,45000) para generar los numeros.
Control: La suma de los numeros generados es 4514159554
El programa debe:
1) Indicar cuantos numeros eran multiplos de 5, cuantos multiplos de 7
y cuantos multiplos de 9
2) Indicar el mayor entre todos aquellos numeros cuyo ultimo digito sea mayor o igual a 5
pero menor o igual a 8.
3) Indicar cuantos numeros generados son pares menores a 15000
4) Indicar el porcentaje entero que representa el punto anterior sobre el total de los numeros procesados.
No se pide el porcentaje redoneanddo, sino truncado sin decimales.
En el calculo de porcentaje haga primero la multiplicacion, luego al division.
INforme caa uno de los resultados, suba el source code con el programa
"""
import random
random.seed(49)
numbers = random.randint(1,45000)
total = 0

for i in range(0,20000):
    print(numbers)

