def validate(inf):
    number = int(input("Ingrese un numero mayor a " + str(inf) + ": "))
    while number <= inf:  # Usar <= para rechazar el 0
        print("Error, se le pidio mayor a", inf, "cargue de nuevo.")
        number = int(input("Ingrese un numero mayor a " + str(inf) + ": "))
    return number


def read(alt):  # Nombre corregido a 'read'
    n = len(alt)
    print("Cargue ahora las alturas del grupo...")
    for i in range(n):
        alt[i] = int(input("Altura[" + str(i) + "]: "))


def average(alt):  # Función faltante agregada
    n = len(alt)
    s = 0
    for i in range(n):
        s += alt[i]
    return s / n  # División flotante con '/'


def compare(heights_array, r2):  # Solo 2 parámetros de entrada
    counter_two = 0
    counter_three = 0
    for i in heights_array:
        if i > r2:
            counter_two += 1
        else:
            counter_three += 1
    return counter_two, counter_three  # Retorna la tupla