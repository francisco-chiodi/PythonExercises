#en el que se cargaban tres números y se pedía determinar cuántos números
#negativos se ingresaron
number_1 = int(input('charge first number: '))
number_2 = int(input('charge second number: '))
number_3 = int(input('charge third number: '))
numbers = number_1, number_2, number_3
negative_counter = 0 #REMEMBER TO PUT THE COUNTER INSIDE THE IF STATEMENT!

if number_1 < 0:
    negative_counter = negative_counter + 1
    print("this is negative ", number_1, "had been ingresed ", negative_counter, "negative numbers")

if number_2 < 0:
    negative_counter = negative_counter + 1

    print("this is negative ", number_2, "had been ingresed ", negative_counter, "negative numbers")

if number_3 < 0:
    negative_counter = negative_counter + 1
    print("this is negative ", number_3, "had been ingresed ", negative_counter, "negative numbers")

#HERE IS THE SOLUTION PROPOSED BY THE PROFESSOR:
"""
a = 0
num = int(input('Ingrese un número: '))
if num < 0:
 a = a + 1

num = int(input('Ingrese otro: '))
if num < 0:
 a = a + 1

num = int(input('Ingrese otro: '))
if num < 0:
 a = a + 1

print('Cantidad de negativos cargados:', a)
"""

