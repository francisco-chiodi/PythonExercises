#Ejercicio 1 Pluviometro
"""
Se ha solicitado un programa que permita cargar las precipitaciones promedio en cada 
mes del país, en base a esos datos armar un menú de opciones que permita:
Determinar el promedio anual de lluvias
Determinar el promedio de lluvias para un determinado trimestre
Determinar el mes más seco del año
Determinar los meses del año en los que llovió más que el promedios de lluvia de todo el año.
"""
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

ceros = 15 * [0]
"""
"""
make a list with n numbers from n 1 to n...
"""
"""
n = 10 #define a superior limit
numbers = [] #receive the numbers
for i in range(1 , n+1):#generate them from 1 to the 11 , so it stop exactly on 10.
                        #remember that is exlusive on the superior limit.
    numbers.append(i) #takes the value of i and add it to the number list.
print("lista original: " ,numbers)
#iterate through the array and fin the even numbers:
for i in range(len(numbers)): #get the total number elements of the list. range will
                              #generate hte list of valid positions to the total count.  
                              #in each iteration i holds the index of the list.   
                              #for i ... assigns one position from that sequence to i on each loop turn.  
    if numbers[i] % 2 == 0: #uses i as the index key to look inside the numbers list and retrieve the value at that position.
        print(numbers[i], end = " ")
"""

"""
 Cargar por teclado un arreglo de n componentes y multiplicarlo por el valor k
que también se ingresa por teclado.
"""
