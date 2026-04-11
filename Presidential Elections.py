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
#date by string
"""
Desarrollar un programa que cargue por teclado una cadena de caracteres que se supone representa
 una fecha en formato'dd/mm/aaaa', y muestre por separado el día, el mes y el año. Ejemplo: si la
  cadena ingresada es '16/03/2016' el programa debe mostrar: 'Día: 16  -  Mes: 03  -  Año: 2016'.
"""
""" 
date = input("input the date on 'dd/mm/aaaa' format")
day = date[0:2]
month = date[3:5]
year = date[6:10]

print("the date is", day, month, year)
"""

"""

 Importe como cadena
Desarrollar un programa que cargue por teclado un importe (cantidad de dinero) expresado como número en
coma flotante y muestre un mensaje con esa cantidad pero en dos formatos: en uno debe aparecer precedida
por el signo '$' y en el otro debe aparecer precedida por la palabra "pesos"."""
#Import by string

"""
quantity = float(input("insert cash " ))
print("$", quantity)
print("pesos", quantity)
"""

"""
Duración de un vuelo
Desarrollar un programa que, conociendo el horario de partida y llegada de un vuelo (hora y minutos), 
determine cuál es su duración en minutos. Si el viajero necesita luego 45 minutos más para ir del 
aeropuerto al hotel que ha reservado, ¿a qué hora llegara al mismo?
"""
#TUPLE EXAMPLE
"""
sec = 4, 6
a, b = sec
print("a: ", a)
print("b: ", b)
"""
"""
a = 12
b = 4
c = a
a = b
b = c
print(a)
print(b)
"""
#FLIGHT TIME
"""
leave = input("input the flight time on hs:min format ")
arrive = input("input the flight arrive time on hs:min format ")
#duration_leave = int(leave[0:1]) , int(leave[4:5])
duration_arrive = int(arrive[0:2]) - int(leave[0:2])
total_mins = duration_arrive * 60 + int(arrive[4:6])
extra_time = 0.45
hotel_arrive = total_mins + extra_time
print("the flight duration is ", total_mins)
print("and you will arrive at your location at " , hotel_arrive)
"""
#ELECTORAL
"""
Control electoral
Desarrollar un programa de control electoral en un centro vecinal, en el que se ingresen,
para cierto candidato: apellido, nombre y cantidad de votos. Luego presentar en pantalla 
un resumen que muestre: iniciales del candidato, cantidad de votos entre paréntesis, 
y debajo una línea con tantas"x" como votos obtenidos (por ejemplo, el candidato obtuvo 4
votos, deberá aparecer una línea como esta:  "xxxx"  con cuatro letras "x") (Asumimos que 
en el centro vecinal nohay demasiados electores, de forma que podamos estar seguros que no
habrá miles o millones de votos... sólo unos pocos para darle sentido al enunciado).
"""
"""
name = input("your name is: ")
last_name = input("your last name is ")
votes = input("enter voters number ")
a, b, c, d = votes[0], votes[1], votes[2], votes[3]



print(name[0], last_name[0],"(", votes, ")\n")
"""