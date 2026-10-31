
"""
Determinar la cantidad de palabras que tienen un dígito en la segunda o en la tercera posición y además
incluyen dos o más consonantes pero a partir de la cuarta posición, incluida la cuarta (en minúscula o
mayúscula). Por ejemplo, en el texto: "Ax1efDa es una password aceptable pero 12r3aei no lo es."
Respuesta: hay solo una palabra que cumple: "Ax1efDa". La palabra "123aei" tiene los dígitos pedidos pero
no tiene ninguna consonante a partir de la cuarta posición, por lo que no cuenta.
"""
m = open("../entrada.txt")
text = m.read()
m.close()


