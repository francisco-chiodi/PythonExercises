"""
 Por cada Sensor se conoce: código de identifi
  cación (cadena de caracteres, combinación de números y letras, por ejemplo SEN001A), ubicación donde se encuentra ins
  talado (cadena de caracteres, por ejemplo Av. Colón y General Paz), tipo de magnitud que evalúa (entero de 1 a 21, po
  r ejemplo 1-Calidad del aire, 2-Flujo vehicular, 3-Estación meteorológica, etc), estado operativo (booleano, si el
   atributo “operativo” es igual a True indica que el sensor se encuentra activo y transmitiendo y, si el atributo
   “operativo” vale False indica que se encuentra fuera de servicio) y consumo energético (decimal, expresado en watts,
    entre 15.5 y 50).
"""
class Service:
    def __init__(self,code,ubi,magnitude,state,con):
        self.code = code
        self.ubi = ubi
        self.magnitude = magnitude
        self.state = state
        self.con = con

    def __str__(self):
        r = ""
        r += "{:<20}".format("el codigo de producto es" + str(self.code))
        r += "{:<20}".format("la descripccion es: " + str(self.ubi))
        r += "{:<20}".format("la cantidad de calorias es:  " + str(self.magnitude))
        r += "{:<20}".format("el tipoo de proucto es:  " + str(self.state))
        r += "{:<20}".format("el precio es: " + str(self.con))

