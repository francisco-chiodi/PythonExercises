with open("tratamientos.txt", "r") as file:
    monto_base_AL = monto_base_MZ = monto_base_U = monto_extra = 0

    for linea in file:


        if linea[0] == "#":
            monto_base_AL = linea[2:8]
            monto_base_MZ = linea[8:14]
            monto_base_U = linea[14:20]
            numeral = linea[0:20]
            continue


        elif "A" <= linea[25] <= "M":
            monto_extra = linea[31:38]
            monto_base = monto_base_AL

        elif "M" <= linea[25] <= "Z":
            monto_extra = linea[31:38]






        print("LINEA AL = ", linea, "AL monto extra =", monto_extra ,"AL monto base =", monto_base_AL, "numeral = " ,numeral)












