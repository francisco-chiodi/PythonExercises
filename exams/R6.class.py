class Banda:
    def __init__(self, nombre, origen, genero, escenario, espectadores):
        self.nombre = nombre
        self.origen = origen
        self.genero = genero
        self.escenario = escenario
        self.espectadores = espectadores

    def __str__(self):
        return f"{self.nombre:<23} - Origen {self.origen:>2} - Género {self.genero:>3} " \
               f"- Escenario: {self.escenario:<15} - Espectadores: {self.espectadores:>6}"
