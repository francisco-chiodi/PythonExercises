"""
Desarrollar un programa que permita cargar un arreglo con las alturas de n
personas. Determinar la altura media del grupo, e informar cuántas de esas personas tienen
altura mayor a la media, y cuántas tienen altura menor o igual a la media

"""
import functionstwo


def test():
    # 1. Definir tamaño y crear arreglo de ceros
    number = functionstwo.validate(0)
    heights_array = number * [0]

    # 2. Cargar alturas directamente en el arreglo
    functionstwo.read(heights_array)
    print("The heights are:", heights_array)

    # 3. Calcular promedio pasándole solo el arreglo
    r2 = functionstwo.average(heights_array)
    print("The average is:", r2)

    # 4. Comparar y contar
    counter_two, counter_three = functionstwo.compare(heights_array, r2)
    print(
        "There are",
        counter_two,
        "persons above average and",
        counter_three,
        "persons below average",
    )


if __name__ == "__main__":
    test()