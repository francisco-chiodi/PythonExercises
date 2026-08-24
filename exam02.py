"""
.1 Determinar la cantidad de palabras que tienen una "x" en la segunda posición.
2. Determinar la longitud de la palabra más larga del texto.
3. Determinar el promedio entero de caracteres por palabra, de las palabras que tienen algún dígito en
cualquier lugar.
4. Determinar cuántas palabras incluyen la expresión "te" en cualquier lugar. Por ejemplo, en el texto: "En
este tejado no se atienen a las normas." hay dos palabras que cumplen: "este" y "tejado". La palabra
"atienen" no cuenta ya que hay una "i" entre la "t" y la "e".

"""
def digit(char):
    return "0" <= char <= "9"
def average(letter_digit,word_digit):
    return  letter_digit//word_digit
def principal():
    m = open("entrada06.txt")
    text = m.read()
    m.close()
    letter = word = r1 = r4 = letter_digit = word_digit = 0
    is_x = False
    r2 = None
    have_digit = False
    is_t = False
    is_te = False
    for char in text:
        if char in " .":
            if letter >= 1:
                word += 1
                if is_x:
                    r1 += 1
                if r2 is None or r2 < letter:
                    r2 = letter

                if have_digit:
                    word_digit += 1

                if is_te:
                    r4 += 1

            letter_digit = letter
            letter = 0
            is_x = False
            is_te = False
            have_digit = False

        else:


            letter += 1
            if char.lower() in "t":
                is_t = True
            else:
                if is_t and char.lower() in "eé": #ataderas
                    is_te = True
                is_t = False

            if letter == 2 and char.lower() in "x":
                is_x = True

            if digit(char):
                have_digit = True
    r3 = average(letter_digit,word_digit)
    print(r1)
    print(r2)
    print(r3 , letter_digit,word_digit)
    print(r4)

if __name__ == "__main__":
    principal()
