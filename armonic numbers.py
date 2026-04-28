#En este primer desafío se pide desarrollar un programa que determine si un número p
# de 6 dígitos (y solo 6 dígitos), es equilibrado por suma de mitades (ESM), inestable,
# ESM armónico o ESM balanceado.

"""
"Un número entero p se dice Equilibrado por Suma de Mitades (ESM) si la suma de los k dígitos de su primera mitad
 es igual a la suma de los k dígitos de la segunda mitad (Ejemplo: p = 234054 es ESM porque 2+3+4 = 9 = 0+5+4
"""
number = input('ingrese un numero de 6 digitos: ')
number_int = int(number)
half_one = int(number[0]) + int(number[1]) + int(number[2])
half_two = int(number[3]) + int(number[4]) + int(number[5])
inverted_number = number[5] + number[4] + number[3] + number[2] + number[1] + number[0]
inverted_int = int(inverted_number)
equilibrium_one = inverted_number[0:3]
equilibrium_two = inverted_number[3:6]
equilibrium = equilibrium_one == equilibrium_two
rest = number_int - inverted_int

if half_one == half_two:
    print('Numero Equilibrado: ', number)
    print('rest: ', rest)
else:
    print('Numero Inestable: ', number)
    print('rest: ', rest)
#si la diferencia entre p y su invertido pi es también ESM
if rest == equilibrium:
    print("equilibrado y armonico: ", rest)
else:
    print("no es equilibrado y armonico", rest)


"""
if rest_half_life == rest_half_two:
    print("Equilibardo y armonico: ", rest)
else:
    print("no es equilibrado y armonico")
#equilibrium = half_one == half_two

"""
"""
c.) Un número entero Equilibrado ESM p, se dice también Armónico, si la diferencia entre p y su
 invertido pi es también ESM (Ejemplo: p = 1313. Es ESM (1+3 = 4 = 1+3). El invertido es pi = 3131.
La diferencia |p - pi| es |1313 - 3131| = 1818es ESM. Por lo tanto, p es Equilibrado (ESM) y Armónico).
d.) Un número entero ESM p, se dice también Balanceado, si la diferencia entre p y su invertido pi NO es también ESM 
(Ejemplo: p = 101020. Es ESM (1+0+1 = 2 = 0+2+0). El invertido es pi = 020101 (agregando un 0 adelante para mantener la
cantidad de dígitos). La diferencia |p - pi| es |10102 - 020101| = 080919 NO es ESM (la suma 0+8+0 = 8 no es igual a la
suma 9+1+9 = 19). Por lo tanto, p es Equilibrado (ESM) y Balanceado). 
"""

