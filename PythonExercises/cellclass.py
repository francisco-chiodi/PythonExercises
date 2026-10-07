"""Empresa celulares
Una empresa dedicada a la venta de líneas para celulares nos pidió un programa que permita realizar una serie de i
nformes. De cada línea se sabe el número, el nombre del titular, el tipo de plan (valor de 0 a 19), la cantidad de
minutos consumidos, y la provincia donde se activó la línea (valor de 1 a 23).
"""
class Cellclass:
    def __init__(self,num,title,plan,quantity,location):
        self.num = num
        self.title = title
        self.plan = plan
        self.quantity = quantity
        self.location = location

    def __str__(self):
        r = (f"el numero es : {self.num:<20} | el titular es: {self.title:<20} | el tipo de plan es: {self.plan:<20} |"
             f"la cantidad de minutos consumidos es: {self.quantity:<20} | la provincia es: {self.location:<20}")
        return r
