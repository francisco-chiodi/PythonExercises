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

xy = lc = add = wc = l4 = result = 0
have_xy = False #pattern design by states.

def is_xy(i):
    if i in "xy":
        return True
    else:
        return False

def average(add,wc):
    result = add//wc
    return result #exit point of the function , it holds and send the value to "variable" at the end of the code
                    #(place where is called)

for i in text:

    if i != " " and i != ".":
        lc += 1

        if is_xy(i) == True:

            have_xy = True #lain from the wired says: like memory , ignores multiple coincidences once one is meet.

    else:
        if lc > 0:
            wc += 1

            add = add + lc # is accumuled by trames, the lc=0 at the end dosent affect it.
            if have_xy == True:
                xy += 1 #only counts the event, not the coincidence.


            if lc > 4:
                l4  += 1

        lc = 0 # this way only counts the letter by word not the total.
        have_xy = False

variable = average(add,wc) #average(add,wc) is replaced by result that holds the value calculated on the function



print("words", wc)
print("words > 4", l4)
print("xy words", xy)
print("average", variable)
#el mono momoxy toca el xilofon.
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


