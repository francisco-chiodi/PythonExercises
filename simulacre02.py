"""
Simulacro 1
Preparación y consignas generales:

c. Se le pedirá que procese una cadena de caracteres cuya carga debe hacerse obligatoriamente desde el
archivo de texto "entrada.txt" según técnicas que fueron explicadas en fichas y en clases prácticas.
d. El texto que cargue desde ese archivo finaliza con "." y cada palabra de ese texto está separada de las
demás por un (y solo un) espacio en blanco.
e. El programa debe incluir una función principal para lanzar el programa desde el script principal.
f. El programa debe tener control de ejecución del script principal con la variable __name__.
g. El programa debe tener al menos una función simple desarrollada por el estudiante con parámetros y con
retorno de resultados.
h. El programa debe procesar el texto caracter a caracter (a razón de uno por vuelta de ciclo, con un único
ciclo para todo el proceso).
secuencia:
print("Primer resultado:", r1)
print("Segundo resultado:", r2)
print("Tercer resultado:", r3)
print("Cuarto resultado:", r4)
 Guarde los resultados que vaya
calculando en las variables r1 (para el primer resultado pedido), y en r2, r3 y r4 respectivamente (para los
resultados que siguen).
Enunciado:
Se pide desarrollar un programa en Python que permita procesar un texto completo contenido en una variable de
tipo cadena de caracteres (cargado desde el archivo "entrada.txt" de acuerdo a todo lo expresado en la sección
anterior), que haga lo siguiente:
1. Determinar la cantidad de palabras comienzan con un dígito impar, pero tales que el resto de sus
caracteres son letras en minúsculas. Por ejemplo, en el texto: "La clave 1alfaxy puede funcionar
en lugar de 1beta9 o en lugar de 9sigmaZ." hay solo una palabra que cumple: "1alfaxy".
2. Determinar la longitud (en cantidad de caracteres) de la palabra más larga entre aquellas que
comienzan con una vocal y contenga al menos una letra "b" (mayúscula o minúscula). Por
ejemplo, en el texto: "Antes de esa esperada circunstancia era imposible." la mayor longitud entre
las palabras que comienzan con vocal es de 9 caracteres (en la palabra "imposible"). Note que la
palabra "circunstancia" tiene más de 9 caracteres, pero no comienza con vocal, por lo que no
debe ser considerada.
Universidad Tecnológica Nacional
Facultad Regional Córdoba
Ing. en Sistemas de Información
EXAMEN PARCIAL 2
Algoritmos y Estructuras de Datos
 Fecha: 2023
Ciclo lectivo: 2023
F0026-W-201102
Hoja: 2 de 1
3. Determinar el promedio entero de caracteres por palabra entre las palabras que tienen más
consonantes que vocales, pero no contienen ninguna "m" ni tampoco ninguna "a". Por ejemplo,
en el texto "Secos los pozos entre tantas mejoras." hay cuatro palabras que cumplen el criterio:
"Secos", "los", "pozos" y "entre", y suman 18 caracteres entre todas ellas. Por lo tanto, el
promedio entero pedido es de 4 letras por palabra.
4. Determinar cuántas palabras incluyen dos o más veces la expresión que conforman la letra "d"
mas una vocal (con cualquiera de sus letras en minúscula o mayúscula) pero de tal forma que la
palabra termine además con una vocal. Por ejemplo, en el texto: "La dadiva va a ser dividida dijo
el pastor." hay dos palabras que cumplen: "dadiva" y "dividida". La palabra "dijo" no cuenta
porque solo tiene una vez la expresión "d" + vocal.

"""
m = open("entrada.txt")
texto = m.read()
m.close()
"""
Determinar la cantidad de palabras comienzan con un dígito impar, pero tales que el resto de sus
caracteres son letras en minúsculas. Por ejemplo, en el texto: "La clave 1alfaxy puede funcionar
en lugar de 1beta9 o en lugar de 9sigmaZ." hay solo una palabra que cumple: "1alfaxy".
"""
odd_digit = w = c  = odd = 0

"""
def lowercase(car):

    if car == int and car % 2 != 0:
        return True
    else:
        return False
"""

for car in texto:
#odd digit , no lower case
    if  car != " " and car !=".":
        c +=1
        """
        is_odd = lowercase(car)
        if is_odd == False:
            print(car)
        """

    if car == " " or car == ".":
        w +=1





















