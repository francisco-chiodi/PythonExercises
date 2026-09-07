class Empleo:
    def __init__(self, cid, des, tip, imp): #self es la instancia. la caja de memoria creada en este instante
        self.identificador = cid #parámetros de entrada que reciben los datos temporales enviados desde el programa principal
        self.descripcion = des #crean atributos permanente, agregando los valores que llegan desde el programa.
        self.tipo = tip
        self.importe = imp

    def __str__(self): #modo de representacon del texto
        """
        Es el método que se invoca de forma implícita cuando haces print(v[i]).
        Su único trabajo es construir y devolver una cadena de texto (string) bien alineada con los datos del objeto.

        """
        r = "" #cadena vacia usada como acumulador
        r = "{:<20}".format("Identificador: " + str(self.identificador)) #"{:<20}".format "reserva un ancho fijo de 20 caracteres y alinea el texto hacia la izquierda (<)".
        r += "{:<35}".format(" - Descripción: " + self.descripcion)
        r += "{:<12}".format(" - Tipo: " + str(self.tipo))
        r += "{:<17}".format(" - Importe: " + str(self.importe))
        return r
