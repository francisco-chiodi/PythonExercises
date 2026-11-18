class Pelicula:
    def __init__(self,codigo,titulo,sala,puntuacion,sinopsis):
        self.codigo = codigo
        self.titulo = titulo
        self.sala = sala
        self.puntuacion = puntuacion
        self.sinopsis = sinopsis

    def __str__(self):
        return(f"codigo: {self.codigo:<20} - titulo: {self.titulo:<20} - sala: {self.sala:<20} - puntuacion: {self.puntuacion:<20}) -sinopsis: {self.sinopsis:<20}")




