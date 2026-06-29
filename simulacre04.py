"""
1)Determinar la cantidad de palabras que tienen un dígito en la segunda y en la cuarta posición, pero de tal
forma que el resto de sus caracteres son letras mayúsculas. Por ejemplo, en el texto: "La pieza D3A5CED
reemplaza a la a4j5TY pero no a la 234DFR." hay solo una palabra que cumple: "D3A5CED". El resto de las
palabras no tienen los dígitos pedidos o tienen alguna minúscula
2)Determinar la longitud (en cantidad de caracteres) de la palabra más corta entre aquellas que comienzan
con una "t" (minúscula o mayúscula). Por ejemplo, en el texto: "Tenemos tantos tios que viajan en tren."
Hay cuatro palabras que comienzan con "t" (minúscula o mayúscula), y la menor longitud entre esas
palabras es de 4 caracteres (en la palabra "tios").
3)Determinar cuántas palabras están conformadas solo por vocales (minúsculas o mayúsculas), pero no
contienen ninguna "u" (minúscula o mayúscula). Por ejemplo, en el texto "Ea pues a por ellos ue ai." hay
tres palabras que cumplen: "Ea", "a" y "ai". La palabra "ue" no cumple porque tiene una "u" (aunque
cumple con estar formada solo por vocales).
"""
def digit(char):
    return "0" <= char <= "9"

def minus(char):
    return "a" <= char <= "z"

def vocal(char):
    return char in "aeiouáéíóú"

def principal():
    m = open("entrada.txt")
    text = m.read()
    m.close()

    letter_counter = word_counter = condition_1 = 0
    valid = True
    is_t = False
    is_short = None
    for char in text:
        if char in " .": #outside word
            word_counter += 1

            if letter_counter >= 1 and is_t == True:
                if is_short is None or is_short > letter_counter:
                    is_short = letter_counter

            if letter_counter >= 4 and valid == True:
                condition_1 += 1

            letter_counter = 0
            valid = True
            is_t = False


        else: #inside word
            letter_counter += 1

            if letter_counter == 1 and char in "tT":
                is_t = True


            if letter_counter == 2:
                if not digit(char):
                    valid = False

            elif letter_counter == 4:
                if not digit(char):
                    valid = False

            else:
                if minus(char) or digit(char):
                    valid = False


    print("r1:",condition_1)
    print("r2:",is_short)
if __name__ == "__main__":
    principal()