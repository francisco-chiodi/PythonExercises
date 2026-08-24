"""
Enunciado:
1. Determinar la cantidad de palabras cuya longitud sea impar, y que tengan solo una consonante
(minúscula o mayúscula). Por ejemplo, en el texto: "Esa chica era Ana y a ese pibe Luis le gustan
las Oreo." hay cinco palabras que cumplen: "Esa", "era", "Ana", "y" y "ese". El resto de las
palabras tiene cantidad par de letras (como "Oreo"), o bien tiene longitud impar pero más de una
consonante (o ninguna). Note que la palabra "y" es válida.
2. Determinar la longitud (en cantidad de caracteres) de la palabra más corta entre aquellas que
tienen una vocal (mayúscula o minúscula) en la segunda posición y no tienen ninguna "n"
(minúscula o mayúscula) en ninguna parte. Por ejemplo, en el texto: "Parece que el precio ni
viene hacia abajo." la menor longitud entre las palabras que cumplen el criterio es de 3 caracteres
Hoja: 2 de 1
(en la palabra "que"). Note que la palabra "ni" tiene menos de 3 caracteres, pero contiene una
"n", por lo que no debe ser considerada.
3. Determinar el promedio entero de caracteres por palabra entre las palabras que tienen una "g"
(minúscula o mayúscula) en la segunda posición y no tienen ningún dígito.
4. Determinar cuántas palabras incluyen la expresión "pe" (con cualquiera de sus letras en
minúscula o mayúscula) pero de tal forma que la palabra además no comience con una vocal
(mayúscula o minúscula).
"""


def odd(number):
    return number % 2 == 1
def cons(char):
    return char.lower() in "bcdfghjklmnpqrstvwxyz"

def average(total,cantidad):
    return total//cantidad



def vocal(char):
    return char.lower() in "aeiouáéíóú"
def digit(char):
    return "0" <=  char <= "9"

def principal():

    m = open("entrada.txt")
    text = m.read()
    m.close()

    w = l = li = c = v = r1 = r2 = r3 = r4 = r3c = total = cantidad = lg = 0

    valid = False
    n = False
    g_valid = False
    r2 = None
    g =  False
    gd = False
    p = False
    pe = False
    v = False

    for char in text:
        if char in " .":
            if l > 0:
                w += 1

                if odd(l) and c == 1:
                    r1 += 1

                if valid and n == False:
                    if r2 is None or r2 > l:
                        r2 = l

                if g == True and gd == False:
                        cantidad += 1


                if not v and pe:
                    r4 += 1


                l = 0
                c = 0
                valid = False
                n = False
                g = False
                gd = False
                pe = False
                p = False
                v = False
        else:
            l += 1
            if cons(char):
                c += 1
            if l == 2 and vocal(char):
                valid = True
            if char.lower() == "n":
                n = True
            if l == 2 and char.lower() == "g":
                g = True
            if g and digit(char):
                gd = True
            if g and gd == False:
                total += 1

            if l == 1 and vocal(char):
                v = True
            if char.lower() == "p":
                p = True
            else:
                if p and char.lower() in "eé":
                    pe = True
                p = False




    r3 = average(total,cantidad)



    print("punto 1: ", r1)
    print("punto 2:", r2)
    print("punto 3:", r3)
    print("punto 4:", r4)







if __name__ == "__main__":
    principal()
