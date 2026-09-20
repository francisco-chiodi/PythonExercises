class Service:
    def __init__(self,id_work,des,types,total,personal_quantity):
        self.id_work = id_work
        self.des = des
        self.type = types
        self.total = total
        self.personal_quantity = personal_quantity

    def __str__(self):
        r = ""
        r += "{:<20}".format("id work is: " + str(self.id_work))
        r += "{:<20}".format("description is : " + str(self.des))
        r += "{:<20".format("type of work is: " + str(self.types))
        r += "{:<20".format("the total import is: "+ str(self.total))
        r += "{:<20}".format("the quantity of empoyes was: " + str(self.personal_quantity))
        return r




"""
Por cada trabajo se tienen los siguientes datos: el número de identificación del trabajo, la descripción o nombre del
mismo, el tipo de trabajo (un valor de 0 a 3, 0: interior, 1: exterior, 2: piletas, 3: tapizados), el importe a cobrar
por ese trabajo y la cantidad de personal afectado para prestar ese servicio.
"""