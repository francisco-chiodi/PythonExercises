class Ticket:
    def __init__(self, flycode,passager_id,destination,seat_number,total):
        self.flycode = flycode
        self.passager_id = passager_id
        self.destination = destination
        self.seat_number = seat_number
        self.total = total


    def __str__(self):
        r = ""
        r = "{:<20}".format("Flycode: " + str(self.flycode))
        r += "{:<35}".format(" - passager id: " + str(self.passager_id))
        r += "{:<12}".format(" - destination: " + str(self.destination))
        r += "{:<17}".format(" - seat number: " + str(self.seat_number))
        r += "{:<17}".format(" - total: " + str(self.total))
        return r
"""
El método __init__ es el constructor de la clase. Se ejecuta automáticamente cada vez que creas un nuevo objeto Ticket.
 Su función principal es asignar los valores recibidos a la nueva instancia:
self: Representa la instancia (el objeto específico) que se está creando en memoria.
self.variable: Crea una propiedad o atributo de objeto. Ese dato quedará guardado dentro del objeto y vivirá mientras
 el objeto exista.
 flycode (sin self): Es una variable local/parámetro. Solo existe dentro de la función __init__ mientras esta se ejecuta
 . Al finalizar el método, esta variable desaparece.

self.flycode (con self): Es el atributo del objeto. La palabra self. le indica a Python que guarde ese valor dentro de
 la estructura interna del objeto.
 Al terminar la ejecución de __init__, los parámetros locales desaparecen de la memoria, pero los datos quedan guardados
  dentro de la instancia a través de los atributos self.*.
  Una instancia es el objeto concreto y real que se crea a partir del molde de una clase.
  La clase Ticket es solo la idea o la plantilla (los planos). Cuando ejecutas mi_ticket = Ticket("AA123", "12345", 
  "Miami", "12A", 500), el valor almacenado en mi_ticket es una instancia: un objeto específico que ocupa un lugar en
   la memoria RAM con sus propios datos. Puedes crear miles de instancias diferentes usando la misma clase.
   Constructor de clase

El constructor es un método especial (__init__ en Python) cuyo único trabajo es construir e inicializar la instancia
 en el momento exacto en que nace.

Cuando pides crear un nuevo objeto, Python realiza dos pasos tras bambalinas:

Reserva el espacio en memoria para el nuevo objeto.

Llama automáticamente al constructor (__init__), pasándole ese objeto recién creado en el parámetro self, junto con 
los datos que le enviaste.

El constructor toma esos datos y "equipa" a la instancia asignándole sus variables internas (self.flycode = flycode,
 etc.). Sin el constructor, la instancia nacería como una estructura vacía sin ningún dato asociado.
"""
