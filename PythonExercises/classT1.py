class Empleo:

    def __init__(self,id,des,types,total):
         self.id = id
         self.des = des
         self.types = types
         self.total= total

    def __str__(self):
        r = ""
        r+= "{:<20}".format("el codigo de identificacion es " + str(self.id))
        r+= "{:<20}".format("la descripcion es " + str(self.des))
        r+= "{:<20}".format("el tipo es " + str(self.types))
        r+= "{:<20}".format("el total es " + str(self.total))
        return r





