"""
 Se cargan por teclado las notas obtenidas por un estudiante en tres parciales
realizados durante el cursado de una materia universitaria. Además, se carga la nota final que ese
estudiante obtuvo en el desarrollo de los trabajos prácticos en esa misma materia. Se sabe que al
terminar el cursado de la materia, todo alumno puede quedar en uno de los siguientes estados
académicos:
a. Libre: si no llegó a cumplir con las condiciones para ser Regular.

b. Regular: si aprobó al menos dos de los tres parciales con nota de 4 o más y además obtuvo
nota de 4 o más en la nota final de trabajos prácticos.

c. Promocionado: si aprobó los tres parciales con nota de 7 o más pero con promedio entre ellos
de 8(ocho) o más, y además obtuvo nota de 8 o más en la nota final del práctico.

d. Aprobado: si aprobó los tres parciales con nota de 7 o más pero con promedio entre ellos de
9(nueve) o más, y además obtuvo nota de 8 o más en la nota final del práctico.
El programa debe determinar y mostrar por pantalla el estado en que finalmente quedó el estudiante.
"""

first_note =  int(input("input the first note: "))
second_note =  int(input("input the second note: "))
third_note =  int(input("input the third note: "))
practice_note = int(input("input the practic note: "))


notes = (first_note + second_note + third_note + practice_note) / 4


if notes < 3.25: #RESTRUCTURA LOS NUMEROS DE MAYOR A MENOR PARA QUE TODAS LAS CONDICIONES SE CUMPLAN FORRO
    print('estas libre bro')
elif notes >= 3.25 and notes < 8:
    print('regular pa')
elif notes >= 9 and practice_note >= 8:
    print('approved')
elif notes >= 8 and practice_note >= 8:
    print('master promotion')





