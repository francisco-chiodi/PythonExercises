class Exercise:
    def __init__(self,name,time_nat,time_cic,time_run):
        self.name = name
        self.time_nat = time_nat
        self.time_cic = time_cic
        self.time_run = time_run

    def __str__(self):
        # f-strings para darle formato alineado a los atributos
        r = f"Nombre: {self.name:<10} | Natación: {self.time_nat:<4} min | Ciclismo: {self.time_cic:<4} min | Carrera: {self.time_run:<4} min"
        return r