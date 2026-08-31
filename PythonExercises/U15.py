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
"""
components =  int(input("components: " ))

components_array = []
for i in range (components + 1):
    components_array.append(components)

multiply =  int(input("multiplycation: " ))

result = components_array * multiply
print("the answer is" , result)
"""
"""
Se ha solicitado un programa que permita cargar las precipitaciones promedio en cada 
mes del país, en base a esos datos armar un menú de opciones que permita:
Determinar el promedio anual de lluvias
Determinar el promedio de lluvias para un determinado trimestre
Determinar el mes más seco del año
Determinar los meses del año en los que llovió más que el promedios de lluvia de todo el año.
"""
def average(total,counter):
    return total//counter

months = [0,1,2,3,4,5,6,7,8,9,10,11]

total_rains = []
presipitations = []
counter = 0 
total_rains = 0 

for i in range (len(months)):

    counter += 1 
    rain = int(input("rain this month: "))
    total_rains += rain

    presipitations.append(rain)
print("average: ", average(total_rains,counter))

select = int(input("trimester selection: "))
if select == 1:
    trimester_data = presipitations[0:3]
elif select == 2:
    trimester_data = presipitations[3:6]
elif select == 3:
    trimester_data = presipitations[6:9]
elif select == 4:
    trimester_data = presipitations[9:12]
else:
    trimester_data = []

if trimester_data:
    total_trimester = 0 
    for rain in trimester_data:
        total_trimester += rain    

    print("promedio del trimestre ", average(total_trimester, len(trimester_data)))

#drier month 

drier_rain = presipitations[0]
drier_month_index = 0 

for i in range(len(presipitations)):
    if presipitations[i] < drier_rain:
        drier_rain = presipitations[i]
        drier_month_index = i 
print("the driest month was:", drier_month_index +1, "with" , drier_rain ,"of rain")

#rains above the anual promedy

annual_average = average(total_rains,counter)
print("months above anual promedy: ", annual_average )
for i in range(len(presipitations)):
    if presipitations[i] > annual_average:
        print("month" ,i + 1, "with" ,presipitations[i], "of rain")
