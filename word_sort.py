"""
Sílaba "mo"
Desarrollar un programa en Python que permita cargar por teclado un texto completo
 (analizar dos opciones: una es cargar
  todo el texto en una variable de tipo cadena de caracteres y recorrerla con un
  for iterador; y la otra es cargar cada caracter uno por uno a través de un while)
  . Siempre se supone que el usuario cargará un punto para indicar el final del texto,
   y que cada palabra de ese texto está separada de las demás por un espacio en blanco.
   El programa debe:

a) Determinar cuántas palabras tenían más de 4 letras.

b) Determinar cuántas palabras tenían al menos una vez la letra "x" o la letra "y".

c) Determinar el promedio de letras por palabra en todo el texto.

d) Determinar cuántas palabras contuvieron sólo una vez la expresión "mo".

********************************************************************************
Ejemplo: 'el mono momoxy toca el xilofon.'
********************************************************************************
Palabras con más de 4 letras: 2
Palabras tenían al menos una vez la letra "x" o la letra "y": 2
El promedio de letras por palabra en todo el texto es: 4.17
Determinar cuántas palabras contuvieron sólo una vez la expresión "mo": 1


"""



text = input("input the text: ")

xy = lc = wc = l4 = 0
have_xy = False

def is_xy(i):
    if i in "xy":
        return True
    else:
        return False

for i in text:

    if i != " " and i != ".":
        lc += 1

        if is_xy(i) == True:

            have_xy = True

    else:
        if lc > 0:
            wc += 1

            if have_xy == True:
                xy += 1


            if lc > 4:
                l4  += 1
        lc = 0
        have_xy = False




print("words", wc)
print("words > 4", l4)
print("xy words", xy)

"""
cl , cp , count_1 = 0
vocal_in_3 = False
def is_vocal(car)
    if car in 'aeiou'
        return True
    return False

for car in text 
    if car == " " or car == ".":
    if cl == 3 or cl == 3 or cl == 7:
        count_1 += 1
        vocal_int_3 = False #reinicio de bandera

    else:
    cl += 1
    if cl == 3 and vocal(car)
        vocal_int_3 = True
    
    
"""


