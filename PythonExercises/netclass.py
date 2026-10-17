import random
"""
Por cada cliente se define: identificación, nombre del titular, tipo de cliente (un valor entre 0 y 8 inclusive), 
 tipo de producto (un valor en 0 y 15 inclusive), monto facturación mensual. A través de un menú de opciones, realizar
 los siguientes puntos:
"""
class Net:
    def __init__(self,iden,name,type_client,type_product,ammount):
        self.iden = iden
        self.name = name
        self.type_client = type_client
        self.type_product = type_product
        self.ammount = ammount

    def __str__(self):
        lines = "=" * 86
        string = (f"| {self.iden:^10} | {self.name:>30} | {self.type_client:^10} | {self.type_product:^10} | {self.ammount:<30} \n |"
                  f"{lines}\n")
        return string

def header():
    lines = "=" * 86
    string = (
        f"{lines} \n"
        f"| {'identificacion':^10} |{'nombre:':>30} | {'tipo cliente':^10} | {'tipo producto:':^10} | {'monto mensual':<30} | \n"
        f"{lines}\n"
    )
    return string
def gen_name():
    name = ('Melvin', 'Marny', 'Vielka', 'Connor', 'Yvette', 'Beard', 'Hahn', 'Beau', 'Spencer', 'Crawford',
            'Duncan', 'Barron', 'Michelle', 'Walton', 'Kirsten', 'Reece', 'Robinson', 'Dylan', 'West')
    lastname = ('Chandler', 'Maxwell', 'Gregory', 'Brooks', 'Burke', 'Meyers', 'Beard', 'Xanthus', 'Crawford',
                'Barron', 'Walton', 'Jenkins', 'Robinson', 'West')
    return f"{random.choice(name)} {random.choice(lastname)}"