"""
Desarrollar un programa que permita cargar un arreglo con las alturas de n
personas. Determinar la altura media del grupo, e informar cuántas de esas personas tienen
altura mayor a la media, y cuántas tienen altura menor o igual a la media

"""
import functionstwo

persons_array = [0,1,2,3,4,5]
heights_array = []
add = 0
counter = 0
counter_two = 0
counter_three = 0

for i in persons_array:
    counter += 1
    height = functionstwo.control()
    heights_array.append(height)
    add += height
print("the heights are:",heights_array)
r2 = functionstwo.average(counter, add)
print("the average is: ", r2)
counter_two , counter_three = functionstwo.compare(heights_array, r2, counter_two, counter_three)
print("there are ", counter_two , "persons above average and", counter_three , "persons below average")
