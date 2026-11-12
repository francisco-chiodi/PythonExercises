class Afiliado:

    def __init__(self, dni, codigo, nivel, tope):

        self.dni = dni
        self.codigo = codigo
        self.nivel = nivel
        self.tope = tope


    def __str__(self):

        cadena = "DNI del afiliado (sin puntos): " + str(self.dni)
        cadena += " | Código de obra social: " + str(self.codigo)
        cadena += " | Nivel de cobertura: " + str(self.nivel)
        cadena += " | Tope por atención: " + str(self.tope)
        return cadena


class Tratamiento:

    def __init__(self, dni, nombre, apellido, codigo, monto_base, complejo, id):

        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.codigo = codigo
        self.monto_base = monto_base
        self.complejo = complejo
        self.id = id

    def __str__(self):
        cadena = "DNI del Paciente (sin puntos): " + str(self.dni)
        cadena += " | Nombre del paciente: " + self.nombre
        cadena += " | Apellido del paciente: " + self.apellido
        cadena += " | Código ICD10: " + self.codigo
        cadena += " | Monto base a pagar por el tratamiento: " + str(self.monto_base)
        cadena += " | Complejidad: " + self.complejo
        cadena += " | ID algoritmo: " + str(self.id)
        return cadena