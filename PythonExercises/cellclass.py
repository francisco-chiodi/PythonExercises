
"""
1. Empresa celulares
Una empresa dedicada a la venta de líneas para celulares nos pidió un programa que permita realizar una serie de informes.
De cada línea se sabe el número, el nombre del titular, el tipo de plan (valor de 0 a 19),
la cantidad de minutos consumidos, y la provincia donde se activó la línea (valor de 1 a 23).
Usted debe realizar dicho programa, controlado por un menú de opciones para que lleve a cabo los siguientes ítems:

"""

class Cell:
    def __init__(self,num,name,plan,minutes,location):
        self.num = num
        self.name = name
        self.plan = plan
        self.minutes = minutes
        self.location = location

    def __str__(self):
        r = (f"Numero: {self.num:<10} | Titular: {self.name:<30} | Tipo de plan: {self.plan:<2} "
             f"| Minutos: {self.minutes:<6} | Provincia: {self.location:2} ")
        #f-string permite evaluar y remplazar variables entre llaves detro de texto
        #:<N alinea el texto a la izquierda y pone espacios vacios a la derecha
        return r
