"""

1)Determinar la cantidad de palabras que tienen un solo dígito y además todo el resto de sus caracteres son
minúsculas. Por ejemplo, en el texto: "El Aer11T2 e2s un cod3igo de in3gre2so CASI i2gual a Aer12T2." hay
tres palabras que cumplen: "e2s", "cód3igo" e "i2gual". Las demás no cuentan porque tienen cero o más
de un dígito o tienen alguna mayúscula.

2)Determinar la longitud (en cantidad de caracteres) de la palabra más corta de aquellas que tienen al
menos un dígito. Por ejemplo, en el texto: "La salida23 aparece marcada en el item92 y en el cuadrante4."
Hay tres palabras con al menos un dígito ("salida23", "item92" y "cuadrante4") y la menor longitud de
entre esas tres, es de 6 caracteres (en la palabra "item92")

3)Determinar cuántas palabras tienen tienen exactamente dos "n" en cualquier lugar (seguidas o no,
mayúsculas o minúsculas) y al menos una "a" (mayúscula o minúscula) pero de forma que esa "a" esté
entre los cuatro primeros caracteres. Por ejemplo, en el texto "La constante None es antagonista de Null."
Hay una palabra que cumple: "antagonista". Las palabras "constante" y "None" no cuentan porque no
tienen una "a" entre los primeros cuatro caracteres (aunque cumplen con tener exactamente dos "n").

4)Determinar cuántas palabras incluyen la expresión "se" (con cualquiera de sus letras en minúscula o
mayúscula) pero de tal forma que la palabra comience con esa expresión y termine con una consonante
cualquiera (en minúscula o mayúscula). Por ejemplo, en el texto: "Sepan que a los semestres los sienten
seguros." Hay tres palabras que cumplen: "Sepan", "semestres" y "seguros". La palabra "sienten"
obviamente no cuenta porque no empieza con "se".

"""

def digit(char):
    return "0" <= char <= "9"
def minus(char):
    return "a" <= char <= "z" or char in "áéíóúüñ"
def cons(char):
    return char.lower() in "bcdfghijklmnñpqrstvwxyz"

def principal():
    m = open("entrada.txt")
    text = m.read()
    m.close()

    count_condition = count_digit = count_char = count_n = count_a = count_p4 = count_p3 = 0
    last_char = ""
    minus_all = True
    has_a = False
    letter = None
    start_se = True
    for char in text:
        if char != " " and char !=".": #inside word

            count_char += 1
            last_char = char

            if count_char == 1 and char not in "sS":
                start_se = False
            if count_char == 2 and char not in "eE":
                start_se = False


            if char in "nN":
                count_n += 1

            if char in "aA" and count_char <= 4:
                has_a = True

            if digit(char):
                count_digit += 1

            if not minus(char) and not digit(char):
                minus_all = False

        else:            #outside word

            if count_char > 0:

                if count_digit >=1:
                    if letter is None or count_char < letter:
                         letter = count_char

                if count_digit == 1 and minus_all == True:
                    count_condition += 1

                if count_n == 2 and has_a:
                    count_p3 += 1

                if start_se and count_char >= 2 and cons(last_char):
                    count_p4 += 1


            #RESETS
            count_digit = 0
            count_char = 0
            count_n = 0
            has_a = False
            start_se = True
            minus_all = True
            last_char = ""


    print("the first condition is met by:",count_condition)
    print("shortest word with a number is:",letter )
    print("3 is:",count_p3 )
    print("4 is:", count_p4)

if __name__ ==  "__main__":
    principal()