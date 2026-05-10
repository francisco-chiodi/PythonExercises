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


