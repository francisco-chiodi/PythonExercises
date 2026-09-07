def read(v):
    array_size = len(v) #calcula len([0,0,0]) , que da 3
    print("cargue los datos del arreglo: ")
    for i in range(array_size): #range(3) , for genera los indices uno a uno
        v[i] = int(input("value" + str(i)))
    #no necesita return prque las listas de python se modifican en memoria
