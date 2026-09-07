"""
Problema 42.) Desarrollar un programa que permita cargar por teclado dos arreglos de
números enteros de n y m componentes respectivamente, y genere y muestre un tercer
arreglo que contenga los valores que aparecen repetidos en los dos arreglos originales. Es
decir, el nuevo arreglo debe contener todos los números que estando en uno de los dos
arreglos originales, están también el otro. Si un número está dos o más veces en el mismo
arreglo (y también figura en el segundo arreglo), sólo debe aparecer una vez en el tercer
arreglo.
"""
import functioncompare
def test():

    #valido que sea mayor a 0
    numbers_v1 = functioncompare.validate(0)

    #creo el arreglo
    v1 = numbers_v1 *[0] #if numbers_v1 is 3 then v1 = [0,0,0]

    #llamo la funcion pasandole el arreglo para que lo llene

    functioncompare.read(v1) #test le entrega [0,0,0] a la funcion read(v), ahora v apunta
                             #a la misma lista en memoria


if __name__ == "__main__":
        test()
