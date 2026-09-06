"""
1. Ordenar y buscar
Se pide un programa que cargue n elementos numéricos
 aleatorios entre 1 y 100 inclusive (pueden existir duplicados).
   A partir de ese arreglo:

Ordenarlo de forma ascendente y mostrarlo
Buscar un elemento x dentro del arreglo (x se ingresa por teclado).
 Si no existe, informarlo. Si existe, determinar cuántos valores
 impares mayores a x se encontraron en el arreglo.

"""

import random
import myfunctions
array = []

for i in range(100):
    number = random.randint(1,100)
    array.append(number)

print("arreglo original: ", array )

myfunctions.selection_sort(array)

print("arreglo ordenado" , array)

x = int(input( "busque un elemento: "))


        
