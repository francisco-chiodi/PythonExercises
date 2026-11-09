"""
Una concesionaria de autos solicita un programa para gestionar sus ventas. Por cada Venta se conoce el nombre del cliente
, el tipo de venta (un valor entre 0 y 3 incluido), marca de auto (un valor entre 1 y 15), la cantidad de cuotas pagas,
el monto total del plan. A través de un menú de opciones, realizar los siguientes puntos:

"""
import random
class Car:
    def __init__(self,name,types,brand,quotes,ammount):
        self.name = name
        self.types = types
        self.brand = brand
        self.quotes = quotes
        self.ammount = ammount

    def __str__(self):
        lines = "=" * 98
        string = ( f"| {self.name:>25} | {self.types:^10} | {self.brand:^10}| {self.quotes:^8} | {self.ammount:>30}\n"
                   f"{lines}\n")
        return string

def header():
    lines = "=" * 98
    string = (f"{lines}\n"
              f"| {'nombre:':>25} | {'tipo de venta:':^10} | {'marca':^10} |  {'cuotas':^8}| {'total:':>25}|\n"
              f"{lines}\n")
    return string

def name_gen():
    name = ('Melvin', 'Marny', 'Vielka', 'Connor', 'Yvette', 'Beard', 'Hahn', 'Beau', 'Spencer', 'Crawford',
            'Duncan', 'Barron', 'Michelle', 'Walton', 'Kirsten', 'Reece', 'Robinson', 'Dylan', 'West')
    lastname = ('Chandler', 'Maxwell', 'Gregory', 'Brooks', 'Burke', 'Meyers', 'Beard', 'Xanthus', 'Crawford',
                'Barron', 'Walton', 'Jenkins', 'Robinson', 'West')
    return f"{random.choice(name)} {random.choice(lastname)}"


