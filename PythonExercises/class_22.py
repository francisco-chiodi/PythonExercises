"""
 se tienen los siguientes datos:
 el número de identificación,
 la descripción del trabajo,
el tipo de trabajo (un número
entero entre 0 y 19, para indicar por ejemplo: 0: siembra, 1: control de plagas, 2: cosecha, etc.)
el importe acobrar por ese trabajo
la cantidad de personal afectado al mismo.
"""
class Trabajo:
    def __init__(self,id_num,des,types,total,personal_quantity):
        self.id_num = id_num
        self.des = des
        self.types = types
        self.total = total
        self.personal_quantity = personal_quantity

    def __str__(self):
        r=""
        r+= "{:<20}".format("el numero de identificacion es " + str(self.id_num))
        r+= "{:<20}".format("descripcion: " + str(self.des))
        r+= "{:<20}".format("el tipo de trabajo es: " + str(self.types))
        r+= "{:<20}".format("el importe a cobrtar por el trabajo es: " + str(self.total))
        r+= "{:<20}".format("la cantidad de personal afectado al mismo es: " + str(self.personal_quantity))
        return r