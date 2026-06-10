with open("tratamientos.txt", "r") as file:
    monto_base_AL = monto_base_MZ = monto_base_U = monto_extra = 0

    for linea in file:


        if linea[0] == "#":
            monto_base_AL = linea[2:8]
            monto_base_MZ = linea[8:14]
            monto_base_U = linea[14:20]
            numeral = linea[0:20]
            continue

        elif "A" <= linea[25] <= "L":
            monto_extra = linea[31:38]
            monto_base = monto_base_AL
            print("LINEA AL:", linea, "AL monto extra =", monto_extra, "AL monto base =", monto_base_AL, "numeral:",
                  numeral)



        elif "M" <= linea[25] <= "Z" and linea[25] != "U":
            monto_extra = linea[31:38]
            monto_base = monto_base_MZ
            print("LINEA MZ:", linea, "MZ monto extra =", monto_extra, "MZ monto base =", monto_base_MZ, "numeral:",
                  numeral)


        elif linea[25] == "U":
            monto_extra = linea[31:38]
            monto_base = monto_base_U
            print("LINEA U:", linea, "U monto extra =", monto_extra, "U monto base:", monto_base_U, "numeral:", numeral)

        """
        print("LINEA AL:",linea, "AL monto extra =", monto_extra ,"AL monto base =", monto_base_AL, "numeral:",numeral)
        print("LINEA MZ:",linea, "MZ monto extra =", monto_extra ,"MZ monto base =", monto_base_MZ, "numeral:",numeral)
        print("LINEA U:",linea, "U monto extra =", monto_extra ,"U monto base:", monto_base_U,"numeral:",numeral)
"""











