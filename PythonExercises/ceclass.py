"""
Una empresa dedicada a la venta de líneas para celulares nos pidió un programa que permita realizar una serie de
 informes. De cada línea se sabe el número, el nombre del titular, el tipo de plan (valor de 0 a 19), la cantidad de
 minutos consumidos, y la provincia donde se activó la línea (valor de 1 a 23).

"""
import random
class Cel:

    def __init__(self,number,name,type_plan,quantity,location):
        self.number = number
        self.name = name
        self.type_plan = type_plan
        self.quantity = quantity
        self.location = location

    def __str__(self):
        lines = "=" * 100
        string = (f"| {self.number:>25} | {self.name:<25} | {self.type_plan:>12} | {self.quantity:>20} | {self.location:>10} \n "
                  f"{lines}\n")
        return string

def header():
    lines = "=" * 100
    string = (f"{lines}\n"
            f"| {'numero':<20} | {'nombre':<25} | {'tipo de plan':>12} | {'minutos consumidos':>20} | {'ciudad':>10} |\n"
              f"{lines}\n")
    return string

def num_gen():
    carac = random.randint(100,900)
    number = random.randint(100000,999999)
    return f"{carac}{number}"
def name_gen():
    name = ("lain","francisco","sofia","tomas","gordoon","leo","santa","julieta","melanie","nahuel","federico","elias")
    lastname = ("ikawura","chiodi","cejas","miente","freeman","messi","loveher","ulman","lazarte","santillan")
    return f"{random.choice(name)} {random.choice(lastname)}"