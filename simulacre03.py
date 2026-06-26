"""

Determinar la cantidad de palabras que tienen un solo dígito y además todo el resto de sus caracteres son
minúsculas. Por ejemplo, en el texto: "El Aer11T2 e2s un cod3igo de in3gre2so CASI i2gual a Aer12T2." hay
tres palabras que cumplen: "e2s", "cód3igo" e "i2gual". Las demás no cuentan porque tienen cero o más
de un dígito o tienen alguna mayúscula.

"""

def principal():
    m = open("entrada.txt")
    text = m.read()
    m.close()
