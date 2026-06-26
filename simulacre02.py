
"""Determinar la cantidad de palabras que tienen un dígito en la segunda o en la tercera posición y además
incluyen dos o más consonantes pero a partir de la cuarta posición, incluida la cuarta (en minúscula o
mayúscula). Por ejemplo, en el texto: "Ax1efDa es una password aceptable pero 12r3aei no lo es."
Respuesta: hay solo una palabra que cumple: "Ax1efDa". La palabra "123aei" tiene los dígitos pedidos pero
no tiene ninguna consonante a partir de la cuarta posición, por lo que no cuenta.
"""
def digit(char):
    return "0" <= char <= "9"
def vocal(char):
    return char in "aeiouáéíóúAEIOUÁÉÍÓÚ"
def con(char):
    return char.lower() in "bcdfghjklmnñpqrstvwxyz"


def principal():

    m = open("entrada.txt")
    text = m.read()
    m.close()
    letter_counter = word_counter = cons_count = count_condition= 0
    is_digit = False

    for char in text:
        if char in " .": # im outside word
            if letter_counter > 0:
                word_counter += 1

                if is_digit and cons_count >=2:
                    count_condition += 1

                letter_counter = 0
                is_digit = False
                cons_count = 0

        else: #im inside word
                letter_counter += 1

                if digit(char) and letter_counter in (2,3):
                    is_digit = True

                if con(char) and letter_counter >= 4:
                    cons_count += 1
    print(count_condition)



if __name__ == "__main__": 
    principal()