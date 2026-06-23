from funciones import *

def principal():
    r1 = r2 = r3 = r4 = r5 = r6 = 0
    acum_cap19 = 0
    cont_cap19 = 0
    r8_nombre = ''
    r9_mayor_importe = 0

    acum_total_general = 0
    cont_alta_complejidad = 0

    monto_adicional_al = monto_adicional_mz = monto_adicional_u = 0

    archivo = open('tratamientos.txt', 'rt')

    for linea in archivo:
        linea_procesada = linea
        if len(linea_procesada) > 1 and linea_procesada[0] == '#':
            monto_adicional_al, monto_adicional_mz, monto_adicional_u = extraer_montos_adicionales(linea_procesada)
        else:
            nombre_paciente, cod_icd10, monto_base, es_alta_complejidad = procesar_paciente(linea_procesada)
            letra, clasificacion, porcentaje_icd10 = procesar_codigo_icd10(cod_icd10)

            monto_final = calcular_importe_final(monto_base, es_alta_complejidad, letra, porcentaje_icd10, monto_adicional_al, monto_adicional_mz, monto_adicional_u)

            r1 += 1
            acum_total_general += monto_final

            if es_alta_complejidad:
                cont_alta_complejidad += 1

            if letra == 'A':
                r2 += 1
            elif letra == 'B':
                r3 += 1
            elif letra == 'C':
                r4 += 1
            elif letra == 'E':
                r5 += 1
            elif letra == 'P':
                r6 += 1

            if letra == 'S' or letra == 'T':
                acum_cap19 += monto_final
                cont_cap19 += 1

            if letra != 'U':
                if monto_final > r9_mayor_importe:
                    r9_mayor_importe = monto_final
                    r8_nombre = nombre_paciente

    archivo.close()

    promedio_general = calcular_promedio(acum_total_general, r1)

    #punto r10
    cont_complejos_superan_prom = 0
    monto_adicional_al = monto_adicional_mz = monto_adicional_u = 0

    archivo = open('tratamientos.txt', 'rt')

    for linea in archivo:
        linea_procesada = linea

        if len(linea_procesada) > 1 and linea_procesada[0] == '#':
                monto_adicional_al, monto_adicional_mz, monto_adicional_u = extraer_montos_adicionales(linea_procesada)
        else:
            nombre_paciente, cod_icd10, monto_base, es_alta_complejidad = procesar_paciente(linea_procesada)
            letra, clasificacion, porcentaje_icd10 = procesar_codigo_icd10(cod_icd10)
            monto_final = calcular_importe_final(monto_base, es_alta_complejidad, letra, porcentaje_icd10, monto_adicional_al, monto_adicional_mz, monto_adicional_u)

            if es_alta_complejidad and monto_final > promedio_general:
                cont_complejos_superan_prom += 1

    archivo.close()

    #Calculos finales y salidas
    r7 = calcular_promedio(acum_cap19, cont_cap19)
    r10 = calcular_porcentaje(cont_complejos_superan_prom, cont_alta_complejidad)

    print('(r1) - Cantidad de tratamientos cargados:', r1)
    print('(r2) - Cantidad de tratamientos "A":', r2)
    print('(r3) - Cantidad de tratamientos "B":', r3)
    print('(r4) - Cantidad de tratamientos "C":', r4)
    print('(r5) - Cantidad de tratamientos "E":', r5)
    print('(r6) - Cantidad de tratamientos "P":', r6)
    print('(r7) – Importe final promedio (capítulo 19):', r7)
    print('(r8) – Paciente (no tipo "U") que pagó el mayor importe final:', r8_nombre)
    print('(r9) - Mayor importe pagado por ese paciente:', r9_mayor_importe)
    print('(r10)- Porcentaje de tratamientos de alta complejidad con coste mayor al promedio:', r10)


if __name__ == '__main__':
    principal()