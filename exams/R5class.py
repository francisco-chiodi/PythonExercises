"""
Una fábrica que vende paquetes de galletas surtidas necesita un programa para gestionar sus productos. Por cada
producto se conoce: el código de producto (un número entero), el tipo de presentación (un entero entre 1 y 10; Ej:
1→Bolsa 400gr, 2→Caja 700gr, etc.), una frase que se incluye al frente del paquete (una cadena terminada en "." con
palabras separadas por un blanco, por ejemplo: "Pruebe nuestras galletas y a-pruebe AED."), la cantidad de sellos de
etiquetado frontal (un entero entre 0 y 4) y el precio sugerido. Se pide:

"""
class Productos:
    def __init__(self,codigo,tipo,frase,sellos,precio):
        self.codigo = codigo
        self.tipo = tipo
        self.frase = frase
        self.sellos = sellos
        self.precio = precio

    def __str__(self):
        return f"codigo: {self.codigo:<20} - tipo: {self.tipo:^10} - frase: {self.frase:<30} - sello: {self.sellos:^10} - precio {self.precio:<20}:"

