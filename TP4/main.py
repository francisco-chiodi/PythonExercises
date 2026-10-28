import os
import coberturas

ARCHIVO_COBERTURAS = 'coberturas.csv'
ARCHIVO_TRATAMIENTOS = 'tratamientos.csv'


def agregar_afiliado_ordenado(v, afiliado):
    n = len(v)
    pos = n
    izq = 0
    der = n - 1

    while izq <= der:
        c = (izq + der) // 2
        if v[c].dni == afiliado.dni:
            pos = c
            break
        if afiliado.dni < v[c].dni:
            pos = c
            der = c - 1
        else:
            izq = c + 1

    v.append(None)
    for i in range(n, pos, -1):
        v[i] = v[i - 1]
    v[pos] = afiliado


def buscar_afiliado_binario(v, dni):
    izq = 0
    der = len(v) - 1

    while izq <= der:
        c = (izq + der) // 2
        if v[c].dni == dni:
            return v[c]
        if dni < v[c].dni:
            der = c - 1
        else:
            izq = c + 1

    return None


def cargar_afiliados():
    v = []
    if os.path.exists(ARCHIVO_COBERTURAS):
        archivo = open(ARCHIVO_COBERTURAS, 'rt', encoding='utf-8')
        cabecera = True
        for linea in archivo:
            if cabecera:
                cabecera = False
                continue
            linea_limpia = linea.strip()
            if linea_limpia != '':
                campos = linea_limpia.split(',')
                dni = int(campos[0])
                cod_obra_social = int(campos[1])
                nivel_cobertura = int(campos[2])
                tope_atencion = float(campos[3])

                afiliado = coberturas.Afiliado(dni, cod_obra_social, nivel_cobertura, tope_atencion)
                agregar_afiliado_ordenado(v, afiliado)
        archivo.close()
    return v


def cargar_tratamientos():
    v = []
    if os.path.exists(ARCHIVO_TRATAMIENTOS):
        archivo = open(ARCHIVO_TRATAMIENTOS, 'rt', encoding='utf-8')
        cabecera = True
        for linea in archivo:
            if cabecera:
                cabecera = False
                continue
            linea_limpia = linea.strip()
            if linea_limpia != '':
                campos = linea_limpia.split(',')
                dni = int(campos[0])
                nombre = campos[1]
                apellido = campos[2]
                cod_icd10 = campos[3]
                monto_base = float(campos[4])
                alta_complejidad = campos[5]
                id_algoritmo = int(campos[6])

                tratamiento = coberturas.Tratamiento(dni, nombre, apellido, cod_icd10, monto_base, alta_complejidad, id_algoritmo)
                v.append(tratamiento)
        archivo.close()
    return v


def mostrar_resultados(v_afiliados, v_tratamientos):
    total_cubierto = 0.0
    total_no_cubierto = 0.0
    cant_tope_aplicado = 0
    cant_no_afiliados = 0

    monto_cubierto_por_os = [0.0] * 21  # Obras sociales indexadas del 1 al 20

    mayor_monto_no_cubierto = -1.0
    dni_mayor_no_cubierto = 0

    for t in v_tratamientos:
        monto_final = t.calcular_monto_final()
        afiliado = buscar_afiliado_binario(v_afiliados, t.dni)

        monto_cubierto, monto_no_cubierto, se_aplico_tope = coberturas.calcular_cobertura_tratamiento(
            monto_final, t.alta_complejidad, afiliado
        )

        total_cubierto += monto_cubierto
        total_no_cubierto += monto_no_cubierto

        if se_aplico_tope:
            cant_tope_aplicado += 1

        if afiliado is None:
            cant_no_afiliados += 1
        else:
            monto_cubierto_por_os[afiliado.cod_obra_social] += monto_cubierto

        if monto_no_cubierto > mayor_monto_no_cubierto:
            mayor_monto_no_cubierto = monto_no_cubierto
            dni_mayor_no_cubierto = t.dni

    # Determinar obra social con mayor monto cubierto (desempate por menor código)
    os_mayor_monto = 1
    monto_os_mayor = monto_cubierto_por_os[1]
    for os_id in range(2, 21):
        if monto_cubierto_por_os[os_id] > monto_os_mayor:
            monto_os_mayor = monto_cubierto_por_os[os_id]
            os_mayor_monto = os_id

    r3_1 = round(total_cubierto, 2)
    r3_2 = round(total_no_cubierto, 2)

    print("r3.1:", r3_1)
    print("r3.2:", r3_2)
    print("r3.3:", cant_tope_aplicado)
    print("r3.4:", cant_no_afiliados)
    print("r3.5:", os_mayor_monto)
    print("r3.6:", dni_mayor_no_cubierto)


def menu():
    print("1. Cargar Afiliados")
    print("2. Cargar Tratamientos")
    print("3. Mostrar Resultados")
    print("0. Salir")
    opc = int(input("Ingrese opción: "))
    return opc


def principal():
    opc = -1
    v_afiliados = None
    v_tratamientos = None

    while opc != 0:
        opc = menu()

        if opc == 1:
            v_afiliados = cargar_afiliados()
        elif opc == 2:
            v_tratamientos = cargar_tratamientos()
        elif opc == 3:
            if v_afiliados is None or v_tratamientos is None:
                print("Error: Debe cargar los afiliados (Opción 1) y los tratamientos (Opción 2) antes de mostrar resultados.")
            else:
                mostrar_resultados(v_afiliados, v_tratamientos)


if __name__ == '__main__':
    principal()
