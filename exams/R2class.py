"""
código (cadena de 5 caracteres alfanuméricos),
• destino (cadena),
• aerolínea (entero entre 1 y 5. 1-Fly Airways, 2-AED te da Alas, 3-Cielos Binarios, 4-Al algoritmo y más allá, 5-
O(n)),
• categoría del hotel reservado para el pasajero (entero entre 1 y 6: 1-Hostel, 2-Económico, 3-3 Estrellas, 4-4
Estrellas, 5-5 Estrellas, 6-Resort),
• precio del paquete completo (valor flotante mayor que 0),
• comentarios del cliente (cadena finalizada en “.” con palabras separadas por 1 espacio).
Sobre la generación de los datos aleatorios
La clase que se pide desarrollar debe llamarse Paquete. El programa debe incluir al menos dos módulos: uno para la
clase y otro para el desarrollo del menú y sus opciones. El módulo del menú debe llamarse principal.py. A continuación
sigue un fragmento de código listo para copiar y pegar en su parcial. Cópielo y péguelo tal cual como se ve, al inicio del
módulo en el que desarrollará el menú:
"""
class Paquete:
    def __init__(self,codigo, destino, aerolinea, categoria, precio, comentario):
        self.codigo = codigo
        self.destino = destino
        self.aerolinea = aerolinea
        self.categoria = categoria
        self.precio = precio
        self.comentario = comentario

    def __str__(self):
        return (f"Codigo {self.codigo:<23} - Desino {self.destino:<20} - aerolinea {self.aerolinea:<20} - categoria {self.categoria:<20}"
                f"precio {self.precio:<20} - Comentarios {self.comentario:<30}")
