"""
Una empresa proveedora de servicios de TV e Internet solicita un programa para gestionar su facturación.
 Por cada cliente se define: identificación, nombre del titular, tipo de cliente (un valor entre 0 y 8 inclusive),
 tipo de producto (un valor en 0 y 15 inclusive), monto facturación mensual. A través de un menú de opciones, realizar
 los siguientes puntos:

"""
import random
class Inter:
    def __init__(self,ide,name,type_client,type_product,ammount):
        self.ide = ide
        self.name = name
        self.type_client = type_client
        self.type_product = type_product
        self.ammount = ammount

    def __str__(self):
        lines = "=" * 86
        string = (f"| {self.ide:<20} | {self.name:<30} | {self.type_client:^10} | {self.type_product:>20} | {self.ammount:>10} |\n"
                  f"|{lines}\n")
        return string

def header():
    lines = "=" * 86
    string = (
        f"{lines} \n"
        f"| {'ide':<20} | {'name':<30} | {'type_client':^10} | {'type_product':>20} | {'ammount':>10} |\n"
        f"|{lines}\n")
    return string

def name_gen():
    name = ('Melvin', 'Marny', 'Vielka', 'Connor', 'Yvette', 'Beard', 'Hahn', 'Beau', 'Spencer', 'Crawford',
            'Duncan', 'Barron', 'Michelle', 'Walton', 'Kirsten', 'Reece', 'Robinson', 'Dylan', 'West')
    lastname = ('Chandler', 'Maxwell', 'Gregory', 'Brooks', 'Burke', 'Meyers', 'Beard', 'Xanthus', 'Crawford',
                'Barron', 'Walton', 'Jenkins', 'Robinson', 'West')
    return f"{random.choice(name)} {random.choice(lastname)}"









