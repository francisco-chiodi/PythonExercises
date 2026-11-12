from clase import *

#opcion 1

def cargar_afiliados(v_afiliados):

    archivo = open("coberturas.csv", "rt")

    archivo.readline()

    for linea in archivo:
        campos = linea.split(",")

        dni = int(campos[0])
        codigo = int(campos[1])
        nivel = int(campos[2])
        tope = float(campos[3])

        a = Afiliado(dni, codigo, nivel, tope)

        add_in_order(v_afiliados, a)

    archivo.close()

def add_in_order(v_afiliados, a):

    izq, der = 0, len(v_afiliados) - 1

    while izq <= der:

        c = (izq + der) // 2

        if v_afiliados[c].dni == a.dni:

            pos = c
            break

        elif v_afiliados[c].dni > a.dni:

            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v_afiliados[pos:pos] = [a]


#opcion 2

def cargar_tratamientos(v_tratamientos):

    archivo = open("tratamientos.csv", "rt")

    archivo.readline()

    for linea in archivo:

        campos = linea.split(",")

        # dni, nombre, apellido, codigo, monto_base, complejo, id

        dni = int(campos[0])
        nombre = campos[1]
        apellido = campos[2]
        codigo = campos[3]
        monto_base = float(campos[4])
        complejo = campos[5]
        id = int(campos[6])

        t = Tratamiento(dni, nombre, apellido, codigo, monto_base, complejo, id)

        v_tratamientos.append(t)

    archivo.close()


#opcion 3

def porcentaje_normal(t):

    partes = t.codigo.split(".")
    porcentaje = int(partes[1]) / 100

    porcentaje_extra = t.monto_base * porcentaje

    return porcentaje_extra


def monto_final(t):

    if t.id == 1:
        return algoritmo_1(t)

    elif t.id == 2:
        return algoritmo_2(t)

    elif t.id == 3:
        return algoritmo_3(t)
    else:
        return algoritmo_normal(t)

def algoritmo_1(t):

    letra_icd10 = t.codigo[0]

    porcentaje_extra = 0
    suma_fija = 0

    if t.monto_base > 60000:

        porcentaje_extra = porcentaje_normal(t)

        if t.complejo == "A" and letra_icd10 != "U":
            suma_fija = t.monto_base / 2

    monto_final = t.monto_base + porcentaje_extra + suma_fija

    return monto_final

def algoritmo_2(t):

    letra_icd10 = t.codigo[0]

    partes = t.codigo.split(".")
    porcentaje = int(partes[1])

    if "A" <= letra_icd10 <= "P":

        porcentaje_extra = porcentaje_normal(t)

    else:

        if t.complejo == "A":

            porcentaje = porcentaje * 2

            porcentaje_extra = (t.monto_base * porcentaje) / 100

        else:

            porcentaje_extra = (t.monto_base * 15) / 100

    monto_final = t.monto_base + porcentaje_extra

    return monto_final

def algoritmo_3(t):

    letra_icd10 = t.codigo[0]

    monto_extra = 0
    monto_fijo = 0

    bloque_icd10 = int(t.codigo[1] + t.codigo[2])

    if t.complejo == "A":
        monto_extra = (t.monto_base * 30) / 100

    if "A" <= letra_icd10 <= "L":

        monto_fijo = 20000

    elif "M" <= letra_icd10 <= "P":

        monto_fijo = 15000 + 5000 * bloque_icd10

    else:

        monto_fijo = (t.monto_base * 10) / 100

    monto_extra += monto_fijo

    if monto_extra > 60000:
        monto_extra = 60000

    monto_final = t.monto_base + monto_extra

    return monto_final

def algoritmo_normal(t):

    letra_icd10 = t.codigo[0]
    partes = t.codigo.split(".")
    porcentaje = int(partes[1])

    monto_con_adicional = t.monto_base + 25000

    if "A" <= letra_icd10 <= "L":
        monto_con_adicional += 25000


    elif "M" <= letra_icd10 <= "Z" and letra_icd10 != "U":
        monto_con_adicional += 40000

    elif letra_icd10 == "U":
        monto_con_adicional += 100000

    porcentaje_extra = (monto_con_adicional * porcentaje) / 100

    monto_final = monto_con_adicional + porcentaje_extra

    return monto_final

def busqueda_binaria(v_afiliados, dni):

    izq, der = 0, len(v_afiliados) - 1

    while izq <= der:

        c = (izq + der) // 2

        if v_afiliados[c].dni == dni:
            return c

        elif v_afiliados[c].dni > dni:

            der = c - 1

        else:
            izq = c + 1

    return -1

def mostrar_resultados(v_afiliados, v_tratamientos):

    total_cubierto = 0
    total_no_cubierto = 0
    cont_tope = 0
    cont_no_afiliados = 0
    mayor_cobertura = 0
    codigo_mayor = 1
    mayor_no_cubierto = 0
    dni_mayor = 0

    acum_obras = [0] * 20

    for i in v_tratamientos:
        montofinal = monto_final(i)

        pos = busqueda_binaria(v_afiliados, i.dni)


        if pos != - 1:
            afiliado = v_afiliados[pos]

            if afiliado.nivel == 1:

                if i.complejo == "R":
                    monto_cubierto = montofinal * 0.50

                else:
                    monto_cubierto = montofinal * 0.40

            elif afiliado.nivel == 2:

                if i.complejo == "R":
                    monto_cubierto = montofinal * 0.70

                else:
                    monto_cubierto = montofinal * 0.60

            elif afiliado.nivel == 3:

                if i.complejo == "R":
                    monto_cubierto = montofinal * 0.90

                else:
                    monto_cubierto = montofinal * 0.80


            if monto_cubierto > afiliado.tope:

                monto_cubierto = afiliado.tope

                cont_tope += 1

            monto_no_cubierto = montofinal - monto_cubierto



            # r3.5
            acum_obras[afiliado.codigo - 1] += monto_cubierto

        else:
            monto_cubierto = 0
            monto_no_cubierto = montofinal

            cont_no_afiliados += 1


        # r3.1 - Monto total cubierto
        total_cubierto += monto_cubierto

        # r3.2 - Monto total no cubierto
        total_no_cubierto += monto_no_cubierto

        # r3.6
        if dni_mayor == 0 or monto_no_cubierto > mayor_no_cubierto:
            mayor_no_cubierto = monto_no_cubierto
            dni_mayor = i.dni

    #r3.5
    for i in range(len(acum_obras)):

        if acum_obras[i] > mayor_cobertura:
            mayor_cobertura = acum_obras[i]
            codigo_mayor = i + 1

    print("r3.1:", round(total_cubierto, 2))
    print("r3.2:", round(total_no_cubierto, 2))
    print("r3.3:", cont_tope)
    print("r3.4:", cont_no_afiliados)
    print("r3.5:", codigo_mayor)
    print("r3.6:", dni_mayor)


def menu():

    print(" 1 - Cargar afiliados")
    print(" 2 - Cargar tratamientos")
    print(" 3 - Mostrar resultados")
    print(" 0 - Salir")

    op = int(input("Ingrese opción: "))
    return op



def principal():

    op = -1

    v_afiliados = []
    v_tratamientos = []

    afiliados_cargados = False
    tratamientos_cargados = False

    while op != 0:

        op = menu()

        if op == 1:
            v_afiliados = []
            cargar_afiliados(v_afiliados)
            afiliados_cargados = True

        elif op == 2:
            v_tratamientos = []
            cargar_tratamientos(v_tratamientos)
            tratamientos_cargados = True

        elif op == 3:

            if afiliados_cargados and tratamientos_cargados:
                mostrar_resultados(v_afiliados, v_tratamientos)
            else:
                print("Error: primero debe cargar ambos archivos.")



if __name__ == '__main__':
    principal()
