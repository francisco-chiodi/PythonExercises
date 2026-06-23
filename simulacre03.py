"""
Preparación y consignas generales:
a. Para comenzar, cree un proyecto en PyCharm y dentro del mismo cree un archivo .py cuyo nombre tenga
el formato legajo-apellido (donde "legajo" es su número de legajo y "apellido" es su apellido).
b. En la misma carpeta de ese proyecto, descargue y guarde el archivo "entrada.txt" que se provee con este
enunciado.
c. Se le pedirá que procese una cadena de caracteres cuya carga debe hacerse obligatoriamente desde el
archivo de texto "entrada.txt" según técnicas que fueron explicadas en fichas y en clases prácticas.
d. El texto que cargue desde ese archivo finaliza con "." y cada palabra de ese texto está separada de las
demás por un (y solo un) espacio en blanco. No hay saltos de línea en el archivo.
e. El programa debe incluir una función principal para lanzar el programa desde el script principal.
f. El programa debe tener control de ejecución del script principal con la variable __name__.
g. El programa debe tener al menos una función simple desarrollada por el estudiante con parámetros y con
retorno de resultados.
h. El programa debe procesar el texto caracter a caracter (a razón de uno por vuelta de ciclo, con un único
ciclo para todo el proceso).
i. El programa que entreguen NO debe usar un menú de opciones ni ningún tipo de carga por teclado en
ninguna parte del programa por ninguna razón. El texto debe ser levantado estrictamente desde el archivo
"entrada.txt".
j. La secuencia y el formato de las instrucciones de salida por pantalla de su programa, debe ser
obligatoriamente y tal cual la que se indica a continuación. No cambie los mensajes, no cambie los
caracteres en cada mensaje, no cambie la forma de cada mensaje, ni cambie el orden de cada print():
print("Primer resultado:", r1)
print("Segundo resultado:", r2)
print("Tercer resultado:", r3)
print("Cuarto resultado:", r4)
k. Copie y pegue las cuatro instrucciones anteriores tal como están al final de su función principal. No
agregue ninguna otra llamada a print() en ninguna parte de su programa. Guarde los resultados que vaya
calculando en las variables r1 (para el primer resultado pedido), y en r2, r3 y r4 respectivamente (para los
resultados que siguen).
Enunciado:
Se pide desarrollar un programa en Python que permita procesar un texto completo contenido en una variable de
tipo cadena de caracteres (cargado desde el archivo "entrada.txt" de acuerdo a todo lo expresado en la sección
anterior), que haga lo siguiente:
1. Determinar la cantidad de palabras que tienen exactamente seis caracteres de largo e incluyen una o dos
vocales (en mayúscula o minúscula) y uno o más dígitos. Por ejemplo, en el texto: "Una simple y curiosa
palabra es kiOs23 pero no aoe8pic." Respuesta: hay 1 palabra que cumple: "kiOs23". La palabra aoe83pic
no cumple porque tiene más de dos vocales y también tiene más de seis caracteres.
2. Determinar el promedio entero de caracteres por palabra, de las palabras que tienen solo una vez una 'r' y
dos o más veces una 'e' (ambas en minúsculas o mayúsculas). Por ejemplo, en el texto: "Entre ellos no hay
respeto ni arenga." hay dos palabras que cumplen el criterio ("Entre" y "respeto"). Entre las dos suman 12
caracteres, por lo que el promedio entero pedido es 6 caracteres por palabra. Note que la palabra
"arenga" no cumple, porque tiene una sola "e" (aunque tiene una "r").
Universidad Tecnológica Nacional
Facultad Regional Córdoba
Ing. en Sistemas de Información
EXAMEN PARCIAL 2
Algoritmos y Estructuras de Datos Fecha: 08/07/2023
Ciclo lectivo: 2023
F0026-W-201102
Hoja: 2 de 1
3. Determinar cuántas palabras empiezan con una vocal y terminan con una vocal pero distinta de la primera
(ambas en minúscula o en mayúscula en forma indistinta). Por ejemplo, en el texto "Ahora aparece esa
chica inclemente y ajena." Hay 3 palabras que cumplen: "aparece", "esa" e "inclemente". Las palabras
"Ahora" y "ajena" no cumplen porque la vocal de comienzo es igual a la de terminación.
4. Determinar cuántas palabras incluyen la expresión "fi" (con cualquiera de sus letras en minúscula o en
mayúscula) y también contienen una "n" o una "t". Por ejemplo, en el texto: "El fino aspecto de ese joven
Faustino y el fieltro que usa lo llevan a la fisura." Hay dos palabras que cumplen: "fino" y "fieltro". La
palabra "fisura" no cuenta porque si bien tiene "fi", no tiene ninguna "n" ni tampoco una "t". Y "Faustino"
tampoco, porque no tiene "fi".
Criterios generales de evaluación.
• Planteo sin carga por teclado en ninguna parte: 0 puntos (reprueba si no cumple).
• Instrucciones de salida tal cual se indicó: 0 puntos (reprueba si no cumple).
• Nombre del archivo fuente correcto: 0 puntos (-1 si no cumple).
• Apertura correcta del archivo "entrada.txt": 0 puntos (-1 si no cumple).
• Planteo en base a un único ciclo: máximo 0 puntos (-2 si no cumple).
• Inclusión correcta de una función principal: máximo 2 puntos.
• Inclusión correcta de al menos una función con parámetros y retorno: máximo 2 puntos.
• Control correcto de ejecución del script principal: máximo 1 punto.
• Resultado correcto del ítem 1: máximo: 3 puntos.
• Resultado correcto del ítem 2: máximo: 4 puntos.
• Resultado correcto del ítem 3: máximo: 5 puntos.
• Resultado correcto del ítem 4: máximo 6 puntos.
• Para aprobar el parcial, el estudiante debe llegar a un mínimo de alrede

"""
"""
1. Determinar la cantidad de palabras que tienen exactamente seis caracteres de largo e incluyen una o dos
vocales (en mayúscula o minúscula) y uno o más dígitos. Por ejemplo, en el texto: "Una simple y curiosa
palabra es kiOs23 pero no aoe8pic." Respuesta: hay 1 palabra que cumple: "kiOs23". La palabra aoe83pic
no cumple porque tiene más de dos vocales y también tiene más de seis caracteres.
"""

def digit(char):
    return "0" <= char <= "9"

def principal():

    m = open("entrada02.txt")
    text = m.read()
    m.close
    new_word = False

    cw = cl = dc= cm = w6 = 0

    w = ""
    charmin = ""

    for char in text:
        if char != " " and char != " .": #dentro de palabra
            cl += 1
            w += char #concateno caracteres
        else:   #sali de palabra , estoy en espacio
            if cl > 0:
                if cl == 6: #veo si cl llego a 6
                    w6 += 1 #cuento que hubo palabra con 6
                    print(w)
                cl = 0

            char = char.lower()

            if char in "aeiouáéíóú":
                cm +=1
                print(cm)

            if char is digit(char):
                dc +=1
                (print, dc)
                #print("palabras con 6 y vocal", w)

                w = ""

        if cl == 6 and dc >= 1 and cm > 1:
            print("test")

        if char == " " or char == " .":
            cw += 1
            new_word = True

if __name__ == "__main__":
    principal()

