#En este primer desafío se pide desarrollar un programa que determine si un número p
# de 6 dígitos (y solo 6 dígitos), es equilibrado por suma de mitades (ESM), inestable,
# ESM armónico o ESM balanceado.

"""
"Un número entero p se dice Equilibrado por Suma de Mitades (ESM) si la suma de los k dígitos de su
 primera mitad
 es igual a la suma de los k dígitos de la segunda mitad (Ejemplo: p = 234054 es ESM porque 2+3+4 = 9
 = 0+5+4

"""
number = input("input the number: ")

sum_1 = int(number[0]) + int(number[1]) + int(number[2])
sum_2 = int(number[3]) + int(number[4]) + int(number[5])

pi_1 = str(number)[5] + str(number)[4] + str(number[3]) + str(number[2]) + str(number[1]) + str(number[0])

harmonic = int(number) - int(pi_1)
harmonic_str = str(harmonic)

if harmonic == 0:
    harmonic_str = "000000"

if str(harmonic_str)[0] == "-":
    sum_harm_1 = int(harmonic_str[1]) + int(harmonic_str[2]) + int(harmonic_str[3])
    sum_harm_2 = int(harmonic_str[4]) + int(harmonic_str[5]) + int(harmonic_str[6])

else:
    sum_harm_1 = int(harmonic_str[0]) + int(harmonic_str[1]) + int(harmonic_str[2])
    sum_harm_2 = int(harmonic_str[3]) + int(harmonic_str[4]) + int(harmonic_str[5])


#234054


if sum_harm_1 == sum_harm_2:
    print("Harmonic")
elif sum_1 == sum_2:
    print("ESM")
else:
    print("Unstable")
"""
print(pi_1)
print(harmonic)
print(sum_harm_1)
print(sum_harm_2)
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

