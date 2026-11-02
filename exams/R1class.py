import random
class r1:
    def __init__(self,id,name,addr,employees, tribute):
        self.id = id
        self.name = name
        self.addr = addr
        self.employees = employees
        self.tribute = tribute
    def __str__(self):
        r = f"identificador: {self.id:<20} | nombre: {self.name:<20} | direccion: {self.addr:<20} | empleados: {self.employees:<20}\n"
        f"impuestos: {self.tribute}"
        return r


def id_gen():
    n = random.randint(1,100)
    return (f"{n}")

def name_gen():
    name = ("tech", "food", "water", "heal", "internet", "sports", "talkative" , "social" , "club")
    return (random.choice(name))

def addres_gen():
    addr = ("avenida neuquen." , "ricardo martinoli." , "buenos aires.", " colon y chacabuco.", " marcelo alvear.")
    return random.choice(addr)

def employee_gen():
    n = random.randint(1,100)
    return n

def tribute_gen():
    n = random.randint(10000,100000)
    return n


