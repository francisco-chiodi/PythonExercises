"""
La Cátedra de AED necesita un programa para controlar las notas finales los alumnos que aprobaron la materia. Por
cada alumno se conoce: legajo (un número entero), nombre y apellido, curso al que asistió (un entero entre 1 y 20),
nota final (un entero entre 6 y 10) y observaciones sobre el alumno (una cadena de caracteres terminada en "." con
palabras separadas con un blanco). Se pide desarrollar un programa que contenga mínimamente dos módulos y un
menú de opciones para las siguientes consignas:
"""
import random
class catedra:

    def __init__(self,legajo,nombre,curso,nota,observaciones):
        self.legajo = legajo
        self.nombre = nombre
        self.curso = curso
        self.nota = nota
        self.observaciones = observaciones

    def __str__(self):
        return(f"legajo: {self.legajo:<20} - nombre y apellido: {self.nombre:<30} - curso: {self.curso:<20} - nota: {self.nota:^10} observaciones: {self.observaciones:<20}")


def legajo():
    legajo = random.randint(1,100)
    return legajo

def nombre():
    nombre = ("fran" , "lain" , "sofi" , "goordon" , "leo" , "anahi" , "mati" , "kira")
    apellido = ("ikawura" , "chiodi" , "freeman" , "half" , "life" ,"wolf" ,"huntsman")
    return random.choice(nombre) + " " + random.choice(apellido)

def curso():
    curso = random.randint(1,20)
    return curso

def nota():
    nota = random.randint(6,10)
    return nota

def observaciones():
    observaciones = ("Excelente rendimiento en todos los parciales.",
    "Un alumno dedicado y muy responsable.",
    "Entregó todos los trabajos prácticos en tiempo.",
    "Obtuvo una nota final destacada en el coloquio.",
    "Participó activamente en clase y obtuvo buenos resultados.",
    "Buen desempeño general durante el cursado anual.",
    "Aprobó sin inconvenientes cada instancia evaluativa.",
    "Impulsó al grupo de trabajo con gran compromiso.",
    "Evidenció un progreso continuo en programación.",
    "El estudiante cumplió con todos los objetivos.")
    return random.choice(observaciones)