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
"""

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
    lc = wc = r1 = l = e = l4 = 0
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
            valid = False
            lc = 0
            l = 0
            e = 0

        else: #letters
            lc += 1
            if lc >= 1:
                if char.isalpha() and lc in (1,2):
                     l += 1
                if is_even(char):
                    e += 1





    print("primer punto",r1)
    print("segundo punto",lcon)
if __name__ == "__main__":
    principal()

