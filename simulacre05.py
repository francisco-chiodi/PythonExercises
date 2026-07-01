"""
Enunciado:
1. Determinar la cantidad de palabras de más de dos caracteres, que tienen letras (minúsculas o mayúsculas)
en las primeras dos posiciones, y luego solo siguen caracteres que representen dígitos pares. Por ejemplo,
en el texto: "Los cuadrantes AC284 y DE983 son peligrosos pero el sector 8U248 es seguro." hay solo una
palabra que cumple: "AC284". La palabra "DE983" tiene un dígito impar y no cumple. La palabra "8U248"
tampoco cumple porque uno de sus dos primeros caracteres es un dígito. Y las palabras "el" y "es" no son
válidas por
2.Determinar la longitud (en cantidad de caracteres) de la palabra más corta entre aquellas que tienen más
de tres caracteres de largo. Por ejemplo, en el texto: "Por fin fuimos campeones del mundo." la menor
longitud entre las palabras que tienen más de tres caracteres es 5 (en la palabra "mundo").
3.Determinar el porcentaje entero (respecto del total de palabras del texto) de las palabras que tienen más
vocales que consonantes. Por ejemplo, en el texto "Ahora esa tarea resulta imposible y torpe." hay tres
palabras que cumplen: "Ahora", "esa" y "tarea". Como hay siete palabras en total en el texto, el porcentaje
entero pedido es del 42 por ciento (aclaración: en el cálculo del porcentaje haga primero la multiplicación
y luego la división).
4.Determinar cuántas palabras incluyen la expresión "tu" (con cualquiera de sus letras en minúscula o
mayúscula) pero de tal forma que la palabra no tenga además ninguna ninguna "b" (minúscula o
mayúscula) ni ningún dígito. Por ejemplo, en el texto: "Los tucumanos tumbaron al ritmo de 2tu y
quedaron en el atium." hay una palabra que cumple: "tucumanos". La palabra "tumbaron" no cuenta
porque si bien tiene la expresión "tu", tiene también una "b". La palabra "2tu" tampoco cuenta porque si
bien tiene "tu", también tiene un dígito. Y "atium" no cuenta porque no tiene "tu".
"""


def percentage(wc,quantity):
    return (quantity * 100) // wc

def vocal(char):
    return char in "aeiouáéíóúAEIOUÁÉÍÓÚ"

def digit(char):
    return "0" <= char <= "9"

def pair(char):
    if digit(char):
        return int(char) % 2 == 0

    return False
def is_even(char):
    return char in "02468"

def principal():
    m = open("entrada.txt")
    text = m.read()
    m.close()
    lc = wc = r1 = l = e = vc = cc = quantity = tu = 0
    valid = False
    lcon = None
    for char in text:
        if char in " .": #words
            wc += 1
            if wc >= 1:
                if l == 2 and lc > 2 and e == lc - 2:
                    r1 += 1
                if lc > 3:
                    if lcon is None or lcon > lc:
                        lcon = lc
                if vc > cc:
                    quantity += 1

                if valid == True:
                    tu += 1


            valid = False
            print("cc:",cc)
            print("cv:",vc)
            print("quantity",quantity)

            lc = 0
            l = 0
            e = 0
            vc = 0
            cc = 0

        else: #letters
            lc += 1
            if lc >= 1:
                if char.isalpha() and lc in (1,2):
                     l += 1
                if is_even(char):
                    e += 1
                if char.isalpha():
                    if vocal(char):
                        vc += 1
                    if not vocal(char):
                        cc += 1
                if char in "tu" and char not in "b":
                    valid = True
                    print(char)


    r3 = percentage(wc, quantity)

    print("primer punto",r1)
    print("segundo punto",lcon)
    print("tercer punto",r3)
    print("cuarto punto",tu)
if __name__ == "__main__":
    principal()

