class Services:
    def __init_(self,id_code,client_name,service_type, total):
        self.id_code = id_code
        self.client_name = client_name
        self.service_type = service_type
        self.total = total
    def str(self): #El método __str__ construye una sola cadena de texto alineada en columnas de ancho fijo para que cada ticket ocupe exactamente una línea limpia en la pantalla.
        r = "" #Inicializa r como una cadena vacía que sirve como "acumulador" donde irás pegando cada sección del ticket.
        r = "{:<20}".format("id: " +str(self.id_code)) #20 reserva columna con ancho fijo de 20 y < indica aliniacion a la izquierda.
        r = "{:<17".format("nombre: " + str(self.client_name))
        r = "{:<35".format("nobre del servicio : " + str(self.service_type))
        r = "{:<17".format("total: " + str(self.total))



""" __init__ es el constructor de la clase. autoamticamente se ejecuta al crear un objeto Services.
 Asigna los valores recibidfos a la instancia , representada por self. Self crea una propiedad/atributo del objeto. 
 vivira mientras guardado mientras el objeto exista.elf. le indica a Python que guarde ese valor dentro de
 la estructura interna del objeto. Al terminar la ejecución de __init__, los parámetros locales desaparecen de la memo
 ria, pero los datos quedan guardados dentro de la instancia a través de los atributos self.*.Una instancia es el objeto
concreto y real que se crea a partir del molde de una clase.
El constructor es un método especial (__init__ en Python) cuyo único trabajo es construir e inicializar la instancia
 en el momento exacto en que nace."""

#Eso quiere decir que ahora el por ejemplo self.id_code = id_code , la informacion queda almacenada permanente en = id_code?