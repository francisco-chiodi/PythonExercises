#Dado el valor de los tres lados del triangulo, calcular su perimetro
"""
side_a = float(input("input the a side: "))
side_b = float(input("input the b side: "))
side_c = float(input("input the c side: "))
sum_sides = side_a + side_b + side_c

print('el perimetro es ', sum_sides)
"""

#Emloyee name and salary by ours

"""
name = "lain"
ours = float (input("horas trabajadas: "))
salary = float (input("salary: "))
multiply = ours * salary
print("the salary of the operator is " , multiply)
"""
"""
#promedy of temperature
temp_one = int (input ("input the first temp: "))
temp_two = int (input ("input the second temp: "))
temp_three = int (input ("input the third temp: "))

temp_sum = temp_one + temp_two + temp_three
promedy_one = temp_sum /3 #float division
promedy_two = temp_sum // 3 #int division

print("the interger promedy is ", promedy_two , "the float promedy is ", promedy_one) #promedy
"""

"""
Cargar por teclado tres números enteros y determinar y mostrar el mayor de ellos. No
utilice para el proceso la función max() de la librería estándar de Python: diseñe el algoritmo
suponiendo que tal función no existe en el lenguaje que usará para el desarrollo del programa.
"""
"""
number_1 = int(input("input number 1: "))
number_2 = int(input("input number 2 "))
number_3 = int(input("input number 3 "))




if number_1 > number_2 and number_1 > number_3:
    print("position 1 is the bigger ", number_1)
elif number_2 > number_1 and number_2 > number_3:
    print("the bigger is position 2")
else:
    print("position 3 is the bigger ", number_3)
"""

"""
Una compañía de alquiler de automóviles necesita un programa que calcule lo que se
debe cobrar a cada cliente, teniendo en cuenta el kilometraje recorrido por el cliente al devolver el
automóvil:
i. Si el cliente no superó los 300 km recorridos se deberá cobrar $500.
ii. Para recorridos desde más de 300 km y hasta no más de 1000 km se le cobrará $500 más el
kilometraje excedente a los 300, a razón de $3 por kilómetro.
iii. Para recorridos mayores a 1000 km se le cobrará $500 más el kilometraje excedente a los
300, a razón de $1.5 por kilómetro. 
"""
""""""
"""
car_kilometers = int(input("kilometers made: "))
excedence = 300
normal_tariff = 500
plus_kilometers = car_kilometers - excedence
plus_tariff = 500 + plus_kilometers * 3
extra_tariff = 500 + plus_kilometers * 1.5



if car_kilometers < 300:
    print("your tariff is ", normal_tariff)
elif car_kilometers > 300 and car_kilometers < 1000:
    print("your tariff is ", plus_tariff )
else:
    print("your tariff is ", extra_tariff)
"""

"""
1. Operaciones de orden con 3 nros.
Realizar un programa que tome tres números, los ordene de mayor a menor. Sobre los valores ordenados diga si 
el tercero es el resto de la división de los dos primeros. 
"""
"""
number_1 = int(input("first number: "))
number_2 = int(input("second number: "))
number_3 = int(input("third number: "))

first_condition = number_1 > number_2 > number_3
second_condition = number_1 > number_3 > number_2
third_condition = number_2 > number_1 > number_3
fourth_condition = number_2 > number_3 > number_1
fifth_condition = number_3 > number_2 > number_1
sixth_condition = number_3 > number_1 > number_2

check_rest_one = number_1 % number_2 == number_3
check_rest_two = number_2 % number_1 == number_3
check_rest_three = number_3 % number_2 == number_1
check_rest_fourth = number_2 % number_3 == number_1
check_rest_five = number_3 % number_1 == number_2
check_rest_sixth = number_1 % number_3 == number_2

if first_condition:
    print("the order is: ", number_1 , number_2 , number_3)
    print("the rest is the third added value", check_rest_one)
elif second_condition:
    print("the orider is: ", number_1, number_3, number_2)
    print("the rest is the third added value", check_rest_sixth)
elif third_condition:
    print("the order is: ", number_2, number_1, number_3)
    print("the rest is the third added value", check_rest_two)
elif fourth_condition:
    print("the order is: ", number_2, number_3, number_1)
    print("the rest is the third added value", check_rest_fourth)
elif fifth_condition:
    print("the order is: ", number_3, number_2, number_1)
    print("the rest is the third added value", check_rest_three)
else:
    print("the order is: ", sixth_condition)
    print("the rest is the third added value", check_rest_five)
"""





