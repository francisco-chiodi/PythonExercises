"""
.1 Determinar la cantidad de palabras que tienen una consonante en la tercera o en la cuarta posición y
además tienen un dígito en cualquier parte.
2. Determinar la longitud de la palabra más corta entre las que comienzan con "s" (minúscula o mayúscula).
3. Determinar el porcentaje entero de palabras (con respecto al total de palabras del texto), de las palabras
que tienen dos o más vocales.
4. Determinar cuántas palabras incluyen una sola vez la expresión "ni" (con cualquiera de sus letras en
minúscula o mayúscula)
"""
def digit(char):
    return "0" <= char <= "9"
def vocal(char):
    return char.lower() in "aeiouáéíóú"

def principal():
    m = open("entrada06.txt")
    text = m.read()
    m.close
    letter = word = 0
    for char in text:

        if char in " .":
            if letter >= 1:
                word += 1
            if is_digit and
            letter = 0
        else:
            letter += 1
            if digit(char):
                is_digit = True
            if letter == 3 and not vocal(char):
                is_vocal = True
            if letter == 4 and not vocal(char):
                is_vocal_2 = True





if __name__ == "__main__":
    principal()
