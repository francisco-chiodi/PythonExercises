from PythonExercises.U15 import MESES


def selection_sort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(i+1, n):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]


def count_odd_greater(v, x):
    counter = 0
    for i in v:
        if i > x and i % 2 != 0:  # Evaluamos 'i' respecto al input
            counter += 1
    return counter


def validation(month_name):  # Validamos que no sea menor a 0
    rain = int(input(f" rain this month for {month_name}: "))
    while rain < 0:
        print("error: cant be negative")
        rain = int(input(f" rain this month for {month_name}: "))
    return rain


def option_rain_charge(v):
    n = len(v)
    for i in range(n):
        v[i] = validation(MESES[i])