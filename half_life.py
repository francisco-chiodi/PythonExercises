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
            cantidad = int(linea[29])
            porcentaje_total = porcentaje_ICD10(cantidad,total)

            print("\nLINEA AL:", linea,
                  "\nAL monto extra:", monto_extra,
                  "\nAL monto base:", monto_base_AL,
                  "\ntotal:", total,
                  "\numeral:", numeral,
                  "\nporcentaje a sacar:", cantidad,
                  "\nporcentaje total:", porcentaje_total)

        elif "M" <= linea[25] <= "Z" and linea[25] != "U":
            monto_extra = int(linea[31:38])
            total = monto_extra + monto_base_MZ
            cantidad = int(linea[29])
            porcentaje_total = porcentaje_ICD10(cantidad,total)

            print("\nLINEA MZ:", linea,
                  "\nMZ monto extra:", monto_extra,
                  "\nMZ monto base:", monto_base_MZ,
                  "\ntotal:", total,
                  "\nnumeral:", numeral,
                  "\nporcentaje a sacar:", cantidad,
                  "\nporcentaje total:", porcentaje_total)


        elif linea[25] == "U":
            monto_extra = int(linea[31:38])
            total = monto_extra + monto_base_U
            cantidad = int(linea[29])
            porcentaje_total = porcentaje_ICD10(cantidad,total)

            print("\nLINEA U:", linea,
                  "\nU monto extra:", monto_extra,
                  "\nU monto base:", monto_base_U,
                  "\ntotal:" ,total,
                  "\nnumeral:", numeral,
                  "\nporcentaje a sacar:", cantidad,
                  "\nporcentaje total:", porcentaje_total)

        """
        print("LINEA AL:",linea, "AL monto extra =", monto_extra ,"AL monto base =", monto_base_AL, "numeral:",numeral)
        print("LINEA MZ:",linea, "MZ monto extra =", monto_extra ,"MZ monto base =", monto_base_MZ, "numeral:",numeral)
        print("LINEA U:",linea, "U monto extra =", monto_extra ,"U monto base:", monto_base_U,"numeral:",numeral)
"""











