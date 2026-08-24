suma = contador = promedio = tratamientos = 0
counter_r2 = counter_r3 = counter_r4 = counter_r5 = counter_r6 = 0
r1 = r2 = r3 = r4 = r5 = r6 = r7 = 0

mayor = -1
linea_mayor_AL = ""

mayor_x = -1
linea_mayor_X = ""

mayor_mz = -1
linea_mayor_mz = ""

mayor_mzx = -1
linea_mayor_mzx = ""


def promedio_19(suma, contador):
    promedio = suma / contador
    return promedio


def porcentaje_x(total):
    total_x = (total * 5) // 100
    return total_x


def porcentaje_ICD10(cantidad, total):
    porcentaje = (total * cantidad) // 100
    return porcentaje


m = open("tratamientos.txt")

monto_base_AL = monto_base_MZ = monto_base_U = monto_extra = 0

for linea in m:
    # Limpiamos el salto de línea para asegurar la posición exacta de la 'X' en el índice 39
    linea = linea.rstrip('\r\n')

    if not linea:
        continue

    if linea[0] == "#":
        monto_base_AL = int(linea[2:8])
        monto_base_MZ = int(linea[8:14])
        monto_base_U = int(linea[14:20])
        numeral = linea[0:20]
        continue

    tratamientos += 1
    r1 = tratamientos
    letra_icd10 = linea[25]

    if letra_icd10 == "A":
        counter_r2 += 1
        r2 = counter_r2
    elif letra_icd10 == "B":
        counter_r3 += 1
        r3 = counter_r3
    elif letra_icd10 == "C":
        counter_r4 += 1
        r4 = counter_r4
    elif letra_icd10 == "D":
        counter_r5 += 1
        r5 = counter_r5
    elif letra_icd10 == "P":
        counter_r6 += 1
        r6 = counter_r6

    if "A" <= linea[25] <= "L":
        # Se ajusta a 30:38 para leer los 8 dígitos enteros del monto base
        monto_extra = int(linea[30:38])
        total = monto_extra + monto_base_AL

        # Extracción del recargo ICD10 (dígito después del punto en la columna 29)
        cantidad = int(linea[29])
        porcentaje_total = porcentaje_ICD10(cantidad, total)

        # El importe inicial incluye el recargo por enfermedad (ICD10)
        importe_final = total + porcentaje_total

        if mayor < importe_final:
            mayor = importe_final
            linea_mayor_AL = linea

        if len(linea) > 39 and linea[39] == "X":
            porcentaje_39 = porcentaje_x(importe_final)
            total_39 = importe_final + porcentaje_39
            importe_final = total_39  # Si tiene X, se actualiza con el 5% extra

            if mayor_x < total_39:
                mayor_x = total_39
                linea_mayor_X = linea

    elif "M" <= linea[25] <= "Z" and linea[25] != "U":
        monto_extra = int(linea[30:38])
        total = monto_extra + monto_base_MZ

        cantidad = int(linea[29])
        porcentaje_total = porcentaje_ICD10(cantidad, total)

        importe_final = total + porcentaje_total

        if mayor_mz < importe_final:
            mayor_mz = importe_final
            linea_mayor_mz = linea

        if len(linea) > 39 and linea[39] == "X":
            porcentaje_39 = porcentaje_x(importe_final)
            total_39 = importe_final + porcentaje_39
            importe_final = total_39  # Si tiene X, se actualiza con el 5% extra

            if mayor_mzx < total_39:
                mayor_mzx = total_39
                linea_mayor_mzx = linea

        # Capitulo 19: promedio (Evaluado correctamente con su importe final corregido)
        if linea[25] == "S" or linea[25] == "T":
            contador += 1
            suma = suma + importe_final
            promedio_total = promedio_19(suma, contador)
            r7 = promedio_total

    elif linea[25] == "U":
        monto_extra = int(linea[30:38])
        total = monto_extra + monto_base_U
        cantidad = int(linea[29])
        porcentaje_total = porcentaje_ICD10(cantidad, total)

        importe_final = total + porcentaje_total

        if len(linea) > 39 and linea[39] == "X":
            porcentaje_39 = porcentaje_x(importe_final)
            total_39 = importe_final + porcentaje_39

m.close()

# --- COMPARACIÓN FINAL AFUERA DEL BUCLE FOR ---
if mayor >= mayor_x and mayor >= mayor_mz and mayor >= mayor_mzx:
    r8 = linea_mayor_AL[0:25]
    r9 = mayor
elif mayor_x >= mayor and mayor_x >= mayor_mz and mayor_x >= mayor_mzx:
    r8 = linea_mayor_X[0:25]
    r9 = mayor_x
elif mayor_mz >= mayor and mayor_mz >= mayor_x and mayor_mz >= mayor_mzx:
    r8 = linea_mayor_mz[0:25]
    r9 = mayor_mz
else:
    r8 = linea_mayor_mzx[0:25]
    r9 = mayor_mzx

print('(r1) - Cantidad de tratamientos cargados:', r1)
print('(r2) - Cantidad de tratamientos "A":', r2)
print('(r3) - Cantidad de tratamientos "B":', r3)
print('(r4) - Cantidad de tratamientos "C":', r4)
print('(r5) - Cantidad de tratamientos "E":', r5)
print('(r6) - Cantidad de tratamientos "P":', r6)
print('(r7) – Importe final promedio (capítulo 19):', r7)
print('(r8) – Paciente (no tipo "U") que pagó el mayor importe final:', r8)
print('(r9) - Mayor importe pagado por ese paciente:', r9)