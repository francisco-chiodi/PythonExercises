"""
Cargar por teclado una lista de números enteros que irán llegando uno a uno, y que
representan cantidades mensuales de automóviles nuevos vendidos en el país durante cierto período.
Para indicar que la carga de datos debe finalizar, se ingresará el valor -1 (menos uno) (note que el
valor 0 (cero) puede ser un dato valido: es perfectamente posible que no haya habido ventas en un
mes determinado). Se pide:
a. Determinar cuántas de esas cantidades fueron mayores o iguales que 0 pero menores que
10000 unidades, cuántas fueron mayores o iguales a 10000 pero menores que 15000, y
cuántas fueron mayores o iguales que 15000.
b. Determinar la cantidad total de automóviles nuevos que se vendieron en el país.
c. Determinar si se ingresó al menos una cantidad igual a 0 o no. Informe con un mensaje simple
en pantalla.
"""

"""
	x = int(input (‘how much do you hate python?: ‘ ) ) 
	s = s + x 
	x = int(input(‘how much do you love assembly?: ‘))
	s = s + x
"""
"""

numbers = 0
data = 0
counter_0 = 0
counter_1 = 0
counter_2 = 0
counter_strike = 0

while numbers != -1:
    numbers = int(input('data numbers: '))

    if data == 0:
        counter_0 = counter_0 + 1

    if data >= 0 < 10000:
        counter_1 = counter_1 + 1
        data = data + numbers

    if data >= 10000 < 15000:
        counter_2 = counter_2 + 1

    if data >= 15000:
        counter_strike = counter_strike + 1


else:
    print("cero units: ", counter_0,  "units > 10000: ",counter_1, "units < 10000 < 15000: ", counter_2, "units > 15000: ", counter_strike)
    print("new cars = ", data )
"""
"""
Complejo de cines
Desarrollar un programa que permita procesar funciones de un complejo de cines. Por cada función se conoce:
 cantidad de espectadores y descuento (S/N). La carga termina cuando la cantidad de espectadores sea igual a 
 0 (cero).

El programa deberá:

a) Calcular la recaudación total del complejo, considerando que el valor de la entrada es de $50 en los días
 con descuento y $75 en los días sin descuento.

b) Determinar cuántas funciones con descuento se efectuaron y qué porcentaje representan sobre el total de 
funciones.
"""

"""
counter_discount = 0
counter_function = 0
discount_function = 0
counter_full = 0
function_full = 0
function_counter = 0
total = 0
discount_accumulator = 0
earns = 0
percentage = 0
quantity = int(input("spectators: "))

while quantity != 0:
    discount = input("discount: ")

    if discount == "S":
        discount_total = 50 * quantity
        discount_accumulator = discount_accumulator + discount_total
        discount_function = discount_function + 1
        function_counter = function_counter + 1

    else:
        full_price = 75 * quantity
        counter_full = counter_full + full_price
        function_full = function_full + 1
        function_counter = function_counter + 1


    quantity = int(input("spectators: "))
    total = discount_accumulator + counter_full


    percentage = (discount_function / function_counter) * 100

print("discount: ", discount_accumulator)
print("discount functions: ", discount_function)
print("full price: ", counter_full)
print("full price functions: ", function_full)
print("functions made: ", function_counter)
print("discount percentage: ", percentage)

print("total earns: ", total)
"""

"""
2. Ventas por sucursal
Ingresar una serie de números por teclado que representan la cantidad de ventas realizadas en las
 diferentes sucursales de un país de una determinada empresa.

Los requerimientos funcionales del programa son:

a) Informar la cantidad de ventas ingresadas.

b) Total de ventas.

c) Cantidad de ventas cuyo valor este comprendido entre 100 y 300 unidades.

d) Cantidad de ventas con 400, 500 y 600 unidades.

e) Indicar si hubo una cantidad de ventas inferior a 50 unidades.

Usted deberá ingresar cantidades de ventas hasta que se ingrese un valor negativo
"""


sales = int(input("input sales: "))
if sales >=0:
    total = int(input("input total: "))
sales_counter = 0
total_accumulator = 0
between_1 = 0
between_2 = 0
between_3 = 0

while sales >= 0:
    sales_counter = sales_counter + sales
    total_accumulator = total_accumulator + total


    if 100 <= sales <= 300:
        between_1 = between_1 + 1

    elif sales == 400 or sales == 500 or sales == 600:
        between_2 = between_2 + 1

    elif sales <= 50:
        between_3 = between_3 + 1


    sales = int(input("input sales: "))
    if sales >=0:
        total = int(input("input total: "))

print("sales: ", sales_counter)
print("total: ", total_accumulator)
print("100-300: ",  between_1)
print("400,500,600: ", between_2)
print("50: ", between_3)

