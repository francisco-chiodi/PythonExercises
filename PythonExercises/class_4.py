class Service:
    def __init__(self,exp_code,des,type,name,total):
        self.exp_code = exp_code
        self.des = des
        self.type = type
        self.name = name
        self.total = total
    def str(self):
        r = ""
        r+= "{:<20}".format("el codigo de expediente es " + str(self.exp_code))
        r+= "{:<20}".format("descripcion: " + str(self.des))
        r+= "{:<20}".format("tipo: " + str(self.type))
        r+= "{:<20}".format("nombre del cliente: " + str(self.name))
        r+= "{:<20}".format("total de los honorarios: " + str(self.total))

