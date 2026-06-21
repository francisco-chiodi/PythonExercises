suma = contador = promedio = 0
mayor = None
linea_mayor_AL = ""

mayor_x = None
linea_mayor_X = ""

mayor_mz = None
linea_mayor_mz = ""

mayor_mzx = None
linea_mayor_mzx = ""

def promedio_19(suma, contador):

    promedio = suma/contador
    return promedio

def porcentaje_x(total):
    total_x = (total * 5) // 100
    return total_x

with open("tratamientos.txt", "r") as file:
    monto_base_AL = monto_base_MZ = monto_base_U = monto_extra = 0

    for linea in file:

        def porcentaje_ICD10(cantidad, total):
            porcentaje = (total * cantidad) // 100
            return porcentaje

        if linea[0] == "#":
            monto_base_AL = int(linea[2:8])
            monto_base_MZ = int(linea[8:14])
            monto_base_U = int(linea[14:20])
            numeral = linea[0:20]

            continue

        elif "A" <= linea[25] <= "L":
            monto_extra = int(linea[31:38])
            total = monto_extra + monto_base_AL
            memo_total = total
            cantidad = int(linea[29])
            porcentaje_total = porcentaje_ICD10(cantidad, total)

            if mayor is None or mayor < total:
                mayor = total
                linea_mayor_AL = linea
            #print("AL",mayor , linea_mayor_AL)


            if linea[39] == "X":
                porcentaje_39 = porcentaje_x(total)
                total_39 = total + porcentaje_39


                if mayor_x is None or mayor_x < total_39:
                    mayor_x = total_39
                    linea_mayor_X = linea

                #print("X",mayor_x ,linea_mayor_X)

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
            porcentaje_total = porcentaje_ICD10(cantidad,total)

            if mayor_mz is None or mayor_mz < total:
                mayor_mz = total
                linea_mayor_mz = linea
            #print("MZ", mayor_mz, linea_mayor_mz)

            #Capitulo 19: promedio
            if linea[25] == "S" or linea[25] == "T":
                contador += 1
                suma = suma + total
                promedio_total = promedio_19(suma, contador)

                """
                print("\ncontador:", contador ,
                      "\nsuma:", suma ,
                      "\npromedio",promedio_total)
                """
            if linea[39] == "X":
                porcentaje_39 = porcentaje_x(total)
                total_39 = total + porcentaje_39

                if mayor_mzx is None or mayor_mzx < total_39:
                    mayor_mzx = total_39
                    linea_mayor_mzx = linea

                #print("MZX", mayor_mzx, linea_mayor_mzx)
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
            porcentaje_total = porcentaje_ICD10(cantidad,total)

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


            

            """
        print("LINEA AL:",linea, "AL monto extra =", monto_extra ,"AL monto base =", monto_base_AL, "numeral:",numeral)
        print("LINEA MZ:",linea, "MZ monto extra =", monto_extra ,"MZ monto base =", monto_base_MZ, "numeral:",numeral)
        print("LINEA U:",linea, "U monto extra =", monto_extra ,"U monto base:", monto_base_U,"numeral:",numeral)
        """
if mayor >= mayor_x and mayor >= mayor_mz and mayor >= mayor_mzx:
    print("El mayor  es AL:", mayor, linea_mayor_AL)
elif mayor_x >= mayor and mayor_x >= mayor_mz and mayor_x >= mayor_mzx:
    print("El mayor  es X:", mayor_x, linea_mayor_X)
elif mayor_mz >= mayor and mayor_mz >= mayor_x and mayor_mz >= mayor_mzx:
    print("El mayor  es MZ:", mayor_mz, linea_mayor_mz)
else:
    print("El mayor  es MZX:", mayor_mzx, linea_mayor_mzx)




"""

S00–S09   Traumatismos de la cabeza

S10–S19   Traumatismos del cuello

S20–S29   Traumatismos del tórax

S30–S39   Traumatismos del abdomen, de la región lumbosacra, de la columna   lumbar y de la pelvis

S40–S49   Traumatismos del hombro y del brazo

S50–S59   Traumatismos del antebrazo y del codo

S60–S69   Traumatismos de la muñeca y de la mano

S70–S79   Traumatismos de la cadera y del muslo

S80–S89   Traumatismos de la rodilla y de la pierna

S90–S99   Traumatismos del tobillo y del pie

T00–T07   Traumatismos que afectan múltiples regiones del cuerpo

T08–T14   Traumatismos de parte no especificada del tronco, miembro o región   del cuerpo

T15–T19   Efectos de cuerpos extraños que penetran por orificios naturales

T20–T32   Quemaduras y corrosiones

T33–T35   Congelamiento

T36–T50   Envenenamiento por drogas, medicamentos y sustancias biológicas

T51–T65   Efectos tóxicos de sustancias de procedencia principalmente no medicinal

T66–T78   Otros efectos y los no especificados de causas externas

T79          Algunas complicaciones precoces de traumatismos

T80–T88   Complicaciones de la atención médica y quirúrgica, no clasificadas en otra parte

T90–T98   Secuelas de traumatismos, de envenenamientos y de otras consecuencias de
causas externas

Este capítulo utiliza la sección 
"""