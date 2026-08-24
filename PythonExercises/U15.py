#Ejercicio 1 Pluviometro
"""
Se ha solicitado un programa que permita cargar las precipitaciones promedio en cada 
mes del país, en base a esos datos armar un menú de opciones que permita:
Determinar el promedio anual de lluvias
Determinar el promedio de lluvias para un determinado trimestre
Determinar el mes más seco del año
Determinar los meses del año en los que llovió más que el promedios de lluvia de todo el año.
"""
def average(total_rain,counter):
    return total_rain/counter 


counter = 0
total_rain = 0
precipitations_list = []
months_array = [0,1,2,3,4,5,6,7,8,9,10,11]

for i in months_array:
    counter += 1
    rain = int(input('precipitaciones: '))
    precipitations_list.append(rain)

    total_rain += rain
print("average:", average(total_rain, counter))