"""
. Determinar la cantidad de palabras que tienen una "x" en la segunda posición. Por ejemplo, en el texto: "El
expresidente es también exjugador y no es xenófobo." hay 2 palabras que cumplen: "expresidente" y
"exjugador". La palabra "xenófobo" tiene una "x" pero no cumple porque la tiene en primera.
Universidad Tecnológica Nacional
Facultad Regional Córdoba
Ing. en Sistemas de Información
EXAMEN PARCIAL 2
Algoritmos y Estructuras de Datos Fecha: 29/06/2024
Ciclo lectivo: 2024
F0026-W-201102
Hoja: 2 de 1
2. Determinar la longitud de la palabra más larga del texto. Por ejemplo, en el texto "La verdad se devela
tarde o temprano." la palabra más larga es "temprano", con 8 caracteres. Por lo tanto, la respuesta para
este ejemplo es 8.
3. Determinar el promedio entero de caracteres por palabra, de las palabras que tienen algún dígito en
cualquier lugar. Por ejemplo, en el texto: "El sector SDR3 acusa un error de la forma E83PC." hay dos
palabras con al menos un dígito("SDR3" y "E83PC"). Entre las dos suman 9 caracteres, por lo que el
promedio entero pedido es 4 caracteres por palabra (promedio = acumulado de la cantidad de letras entre
las palabras que cumplen // cantidad de palabras que cumplen).
4. Determinar cuántas palabras incluyen la expresión "te" en cualquier lugar. Por ejemplo, en el texto: "En
este tejado no se atienen a las normas." hay dos palabras que cumplen: "este" y "tejado". La palabra
"atienen" no cuenta ya que hay una "i" entre la "t" y la "e".

"""
def principal():
    m = open("entrada06.txt")
    text = m.open()
    m.close()
    letter = word = 0
    for char in text:
        if char in " .":
            if letter >= 1:
                word += 1
        else:
            letter += 1
    print(letter)
if __name__ == "__main__":
    principal()