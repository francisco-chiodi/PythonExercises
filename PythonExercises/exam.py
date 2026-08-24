"""
.1Determinar la cantidad de palabras comienzan con un dígito impar, pero tales que el resto de sus
caracteres son letras en minúsculas.
2. Determinar la longitud (en cantidad de caracteres) de la palabra más larga entre aquellas que
comienzan con una vocal y contenga al menos una letra "b" (mayúscula o minúscula).

3. Determinar el promedio entero de caracteres por palabra entre las palabras que tienen más
consonantes que vocales, pero no contienen ninguna "m" ni tampoco ninguna "a".
4. Determinar cuántas palabras incluyen dos o más veces la expresión que conforman la letra "d"
mas una vocal (con cualquiera de sus letras en minúscula o mayúscula) pero de tal forma que la
palabra termine además con una vocal.
"""
"""
anterior), que haga lo siguiente:
1. Determinar la cantidad de palabras cuya longitud sea par, y que estén conformadas por vocales y
consonantes en partes iguales (minúsculas o mayúsculas). 
2. Determinar la longitud (en cantidad de caracteres) de la palabra más larga entre aquellas que
tienen al menos un dígito y no tienen una "p" (mayúscula o minúscula).
3. Determinar el promedio entero de caracteres por palabra entre las palabras que tienen más de
dos caracteres pero incluyen una o más veces una "s". 
4. Determinar cuántas palabras incluyen la expresión "ra" (con cualquiera de sus letras en minúscula
o mayúscula) pero de tal forma que la palabra además tenga una vocal (mayúscula o minúscula)
entre sus dos primeros caracteres. P
"""
def even(letter):
    return letter % 2 == 0
def digit(char):
    return "0" <= char <= "9"
def vocal(char):
    return char.lower() in "aeiouáéíóú"
def average(letter_r3,word_r3):
    return letter_r3//word_r3
def cons(char):
    return char.lower() in "bcdfghjklmnñpqrstvwxyz"
def principal():
    m = open("entrada04.txt")
    text = m.read()
    m.close()
    letter = word=r44 = word_r3 = r1 = letter_r3 = r4 = vocal_counter = cons_counter = 0
    is_digit = False
    vocal_1 = False
    vocal_2 = False
    is_p = False
    is_r = False
    is_ra = False
    r2 = None
    third_condition = False
    for char in text:
        if char in " .":

            if letter >= 1:
                word += 1
                if even(letter):
                    if vocal_counter == cons_counter:
                        r1 += 1

                if not is_p and is_digit:
                    if r2 is None or r2 < letter:
                        r2 = letter

                if third_condition:
                    word_r3 += 1

                if is_ra:
                    r4 += 1


            letter = 0
            vocal_counter = 0

            cons_counter = 0
            is_ra = False
            vocal_1 = False
            vocal_2 = False
            is_digit = False
            third_condition = False
        else:
            letter += 1
            if letter >= 2:
                if char.lower() in "s":
                    third_condition = True
                    letter_r3 += 1
            if letter == 1 and vocal(char):
                vocal_1 = True
            if letter == 2 and vocal(char):
                vocal_2 = True

            if vocal_1 or vocal_2:
                if char.lower() in "r":
                    is_r = True
                else:
                    if is_r and char.lower() in "aá":  # esperada
                        is_ra = True
                    is_r = False

            if vocal(char):
                vocal_counter += 1
            if cons(char):
                cons_counter += 1

            if char.lower() in "p": #pa1
                is_p = True
            if digit(char):                 # pa1
                is_digit = True
    r3 = average(letter_r3,word_r3)

    print("primer punto: ", r1)
    print("segundo punto: ", r2)
    print("tercer punto :", r3)
    print("cuarto punto:", r4)
"""
4)Determinar cuántas palabras incluyen la expresión "ra" (con cualquiera de sus letras en minúscula
o mayúscula) pero de tal forma que la palabra además tenga una vocal (mayúscula o minúscula)
entre sus dos primeros caracteres
"""




if __name__ == "__main__":
    principal()