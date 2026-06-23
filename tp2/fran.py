suma = contador = promedio = tratamientos = 0
counter_r2 = counter_r3 = counter_r4 = counter_r5 = counter_r6 = 0
r1 = r2 = r3 = r4 = r5 = r6 = r7 = 0
mayor = None
linea_mayor_AL = ""

mayor_x = None
linea_mayor_X = ""

mayor_mz = None
linea_mayor_mz = ""

mayor_mzx = None
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
        # print("A", linea)
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
        monto_extra = int(linea[31:38])
        total = monto_extra + monto_base_AL
        memo_total = total
        cantidad = int(linea[29])
        porcentaje_total = porcentaje_ICD10(cantidad, total)

        if mayor is None or mayor < total:
            mayor = total
            linea_mayor_AL = linea
        # print("AL",mayor , linea_mayor_AL)

        if linea[39] == "X":
            porcentaje_39 = porcentaje_x(total)
            total_39 = total + porcentaje_39

            if mayor_x is None or mayor_x < total_39:
                mayor_x = total_39
                linea_mayor_X = linea

                # print("X",mayor_x ,linea_mayor_X)

                """
                print("\nx total ", total_39 ,
                      "\nlinea x" ,linea ,
                      "\ntotal original: ", total,
                      "\nporcentaje 5%", porcentaje_39)
                """
            """
            print("\nLINEA AL:", linea,
                  "\nAL monto extra:", monto_extra,
                  "\nAL monto base:", monto_base_AL,
                  "\ntotal:", total,
                  "\numeral:", numeral,
                  "\nporcentaje a sacar:", cantidad,
                  "\nporcentaje total:", porcentaje_total)
            """
    elif "M" <= linea[25] <= "Z" and linea[25] != "U":
        monto_extra = int(linea[31:38])
        total = monto_extra + monto_base_MZ
        cantidad = int(linea[29])
        porcentaje_total = porcentaje_ICD10(cantidad, total)

        if mayor_mz is None or mayor_mz < total:
            mayor_mz = total
            linea_mayor_mz = linea
            # print("MZ", mayor_mz, linea_mayor_mz)

            # Capitulo 19: promedio
        if linea[25] == "S" or linea[25] == "T":
            contador += 1
            suma = suma + total
            promedio_total = promedio_19(suma, contador)
            r7 = promedio_total
            """
            print("\ncontador:", contador,
                  "\nsuma:", suma,
                  "\npromedio", promedio_total)
            """

        if linea[39] == "X":
            porcentaje_39 = porcentaje_x(total)
            total_39 = total + porcentaje_39

            if mayor_mzx is None or mayor_mzx < total_39:
                mayor_mzx = total_39
                linea_mayor_mzx = linea

            # print("MZX", mayor_mzx, linea_mayor_mzx)
            """
            print("\nx total MZ ", total_39 ,
                    "\nlinea x MZ" ,linea ,
                    "\ntotal original MZ: ", total,
                    "\nporcentaje 5% MZ", porcentaje_39)
            """

            """
            print("\nLINEA MZ:", linea,
                  "\nMZ monto extra:", monto_extra,
                  "\nMZ monto base:", monto_base_MZ,
                  "\ntotal:", total,
                  "\nnumeral:", numeral,
                  "\nporcentaje a sacar:", cantidad,
                  "\nporcentaje total:", porcentaje_total)
            """
    elif linea[25] == "U":
        monto_extra = int(linea[31:38])
        total = monto_extra + monto_base_U
        cantidad = int(linea[29])
        porcentaje_total = porcentaje_ICD10(cantidad, total)

        if linea[39] == "X":
            porcentaje_39 = porcentaje_x(total)
            total_39 = total + porcentaje_39

            """
                print("\nx total U ", total_39 ,
                      "\nlinea x" ,linea ,
                      "\ntotal original U: ", total,
                      "\nporcentaje 5% U", porcentaje_39)
                """
            """
            print("\nLINEA U:", linea,
                  "\nU monto extra:", monto_extra,
                  "\nU monto base:", monto_base_U,
                  "\ntotal:" ,total,
                  "\nnumeral:", numeral,
                  "\nporcentaje a sacar:", cantidad,
                  "\nporcentaje total:", porcentaje_total)

            """

if mayor >= mayor_x and mayor >= mayor_mz and mayor >= mayor_mzx:
    r8 = linea_mayor_AL
    r9 = mayor
    # print("El mayor  es AL:", mayor, linea_mayor_AL)
elif mayor_x >= mayor and mayor_x >= mayor_mz and mayor_x >= mayor_mzx:
    r8 = linea_mayor_X
    r9 = mayor_x
    # print("El mayor  es X:", mayor_x, linea_mayor_X)
elif mayor_mz >= mayor and mayor_mz >= mayor_x and mayor_mz >= mayor_mzx:
    r8 = linea_mayor_mz
    r9 = mayor_mz
    # print("El mayor  es MZ:", mayor_mz, linea_mayor_mz)
else:
    r8 = linea_mayor_mzx
    r9 = mayor_mzx
    # print("El mayor  es MZX:", mayor_mzx, linea_mayor_mzx)

texto = m.read()
m.close()

print('(r1) - Cantidad de tratamientos cargados:', r1)
print('(r2) - Cantidad de tratamientos "A":', r2)
print('(r3) - Cantidad de tratamientos "B":', r3)
print('(r4) - Cantidad de tratamientos "C":', r4)
print('(r5) - Cantidad de tratamientos "E":', r5)
print('(r6) - Cantidad de tratamientos "P":', r6)
print('(r7) – Importe final promedio (capítulo 19):', r7)
print('(r8) – Paciente (no tipo "U") que pagó el mayor importe final:', r8)
print('(r9) - Mayor importe pagado por ese paciente):', r9)
# print('(r10)- Porcentaje de tratamientos de alta complejidad con coste mayor al promedio:', r10)