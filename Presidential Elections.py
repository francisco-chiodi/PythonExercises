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
car_kilometers = int(input("kilometers made: "))
excedence = 300
normal_tariff = 500
plus_kilometers = car_kilometers - excedence
plus_tariff = 500 + plus_kilometers * 3



if car_kilometers < 300:
    print("your tariff is ", normal_tariff)
elif car_kilometers > 300 and car_kilometers < 1000:
    print("your tariff is ", plus_tariff  )






