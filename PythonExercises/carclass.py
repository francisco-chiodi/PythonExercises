import random

class Carclass:
    def __init__(self,name,types,brand,quote,total):
        self.name = name
        self.types = types
        self.brand = brand
        self.quote = quote
        self.total = total

    def __str__(self):
        line = "=" * 81
        string = f"| {self.name:>30} | {self.types:^20} | {self.brand:>20} | {self.quote:^10} | {self.total:<20}|\n"
        f"{line:<86}\n"
        return string

def header():
    line = "=" * 81

    string = f"{line:>80}  \n " \
                f"| {'nombre':>30} | {'tipo de venta':^20} | {'marca':>20} | {'cuota':^10} | {'total':<20} \n " \
                f"{line:>80} \n"
    return string

def gen_name():
    nombres = ('Melvin', 'Marny', 'Vielka', 'Connor', 'Yvette', 'Beard', 'Hahn', 'Beau', 'Spencer', 'Crawford',
                   'Duncan', 'Barron', 'Michelle', 'Walton', 'Kirsten', 'Reece', 'Robinson', 'Dylan', 'West')

    apellidos = ('Chandler', 'Maxwell', 'Gregory', 'Brooks', 'Burke', 'Meyers', 'Beard', 'Xanthus', 'Crawford',
                     'Barron', 'Walton', 'Jenkins', 'Robinson', 'West')
    return f"{random.choice(nombres)} {random.choice(apellidos)}"

#def gen_num():
    return f"{random.randint(350, 373)}{random.randint(1, 9)}{random.randint(111111, 999999)}"