def extraer_montos_adicionales(linea):
    monto_al = monto_mz = monto_u = ''
    posicion = 0

    for car in linea:
        if '0' <= car <= '9':
            if 2 <= posicion <= 7:
                monto_al += car
            elif 8 <= posicion <= 13:
                monto_mz += car
            elif 14 <= posicion <= 19:
                monto_u += car
        posicion += 1

    return int(monto_al), int(monto_mz), int(monto_u)

def procesar_paciente(linea):
    posicion = 0
    es_alta_complejidad = False
    nombre_paciente = cod_icd10 = monto_base = espacios_pendientes = ''

    for car in linea:
        if posicion <= 24:
            if car == ' ':
                espacios_pendientes += car
            else:
                if espacios_pendientes != '':
                    nombre_paciente += espacios_pendientes
                    espacios_pendientes = ''
                nombre_paciente += car
        elif 24 < posicion <= 30:
            if car != ' ':
                cod_icd10 += car
        elif 30 < posicion <= 38:
            if car != ' ':
                monto_base += car
        elif posicion == 39 and car == 'X':
            es_alta_complejidad = True

        posicion += 1

    if monto_base != '':
        monto_base = int(monto_base)
    else:
        monto_base = 0
    return nombre_paciente, cod_icd10, monto_base, es_alta_complejidad

def procesar_codigo_icd10(cod_icd10):
    bd_paso_punto = False
    letra = ''
    clasificacion = ''
    porcentaje = ''

    for car in cod_icd10:
        if car != ' ':
            if 'A' <= car <= 'Z' and letra == '':
                letra = car
            elif '0' <= car <= '9' and not bd_paso_punto :
                clasificacion += car
            elif car == '.':
                bd_paso_punto = True
            elif '0' <= car <= '9' and bd_paso_punto:
                porcentaje += car
    if clasificacion != '':
        clasificacion = int(clasificacion)
    else:
        clasificacion = 0

    if porcentaje != '':
        porcentaje = int(porcentaje)
    else:
        porcentaje = 0

    return letra, clasificacion, porcentaje

def calcular_recargo(porcentaje, importe_sobre_el_que_aplica):
    return (importe_sobre_el_que_aplica * porcentaje) / 100

def calcular_porcentaje(cantidad_parcial, cantidad_total):
    if cantidad_total == 0:
        return 0
    return (cantidad_parcial * 100) // cantidad_total

def calcular_promedio(acumulador, contador):
    if contador == 0:
        return 0
    promedio = acumulador / contador
    return round(promedio, 2)

def calcular_monto_letra(letra, monto_al, monto_mz, monto_u):
    monto_adicional = 0
    if 'A' <= letra <= 'L':
        monto_adicional += monto_al
    elif 'M' <= letra <= 'Z' and letra != 'U':
        monto_adicional += monto_mz
    elif letra == 'U':
        monto_adicional += monto_u
    return monto_adicional

def calcular_importe_final(monto_base, es_complejo, letra, porcentaje_icd10, monto_al, monto_mz, monto_u):
    monto_final = monto_base

    monto_final += calcular_monto_letra(letra, monto_al, monto_mz, monto_u)

    monto_final += calcular_recargo(porcentaje_icd10, monto_final)

    if es_complejo:
        monto_final += calcular_recargo(5, monto_final)

    return monto_final
