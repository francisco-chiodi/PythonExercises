
with open("tratamientos.txt", "r") as file:
    treatments = 0
    counter_r2 = 0
    counter_r3 = 0
    counter_r4 = 0
    counter_r5 = 0
    counter_r6 = 0
    in_block_1 = False
    in_block_2 = False
    in_block_3 = False

    for line in file:
        treatments += 1
        #              BLOCK1
        if line[0:20] == "# 296645352478207261":
            in_block_1 = True
            base_amount_AL = line[2:8]
            base_amount_MZ = line[8:14]
            base_amount_U = line[14:20]
            numcheck = line[0:20]
            continue

        if "A" <= line[25:30] <= "L" and in_block_1 == True:
            extra_amount_AL = line[31:38]
            print("line 1 AL:", line, "base mount 1 AL:",base_amount_AL, "numcheck block 1:", numcheck, "extra mount 1 AL:",extra_amount_AL)


        if "M" <= line[25:30] <= "Z" and in_block_1 == True and line[0] != "U":
            extra_amount_MZ = line[31:38]
            print("line 1 MZ !=U =", line, "base amount 1 =",base_amount_MZ,"numcheck block 1=", numcheck, "extra mount 1 MZ=",extra_amount_MZ )
            #total_1 = base_mount_MZ + extra_mount_AL
        elif "M" <= line[25:30] <= "Z" and in_block_1 == True and line[0] == "U":
            print("line 3 U", line, "base amount 1 U",base_amount_U , "numcheck", numcheck, "extra amount",extra_amount_MZ)



        #              BLOCK2


        if line[0:20] == "# 196645252478107261":
            in_block_1 = False
            in_block_2 = True
            numcheck = line[0:20]
            base_amount_AL = line[2:8]
            base_amount_MZ = line[8:14]
            base_amount_U = line[14:20]
            continue

        if "A" <= line[25:30] <= "L" and in_block_2 == True:
            extra_amount_AL = line[31:38]
            print("line 2 AL:", line, "base amount 2 AL:",base_amount_AL, "numcheck:",numcheck,"extra amount 2 AL",extra_amount_AL)

        if "M" <= line[25:30] <= "Z" and in_block_2 == True and line[25] != "U":
            extra_amount_MZ = line[31:38]
            print("line 2 MZ !=U:", line, "base amount 2 MZ:",base_amount_MZ , "numcheck:", numcheck, "extra mount 2 MZ:",extra_amount_MZ)

        elif "M" <= line[25:30] <= "Z" and in_block_2 == True and line[25] == "U":
            extra_amount_MZ = line[31:38]
            print("line 2 U:", line, "base amount 2 MZ:",base_amount_U , "numcheck:", numcheck, "extra mount 2 MZ:",extra_amount_MZ)



        #              BLOCK3
        if line[0:20] == "# 48500 62953 294690":
            in_block_1 = False
            in_block_2 = False
            in_block_3 = True
            numcheck = line[0:20]
            base_amount_AL = line[2:8]
            base_amount_MZ = line[8:14]
            base_amount_U = line[14:20]
            continue


        if "A" <= line[25:30] <= "L" and in_block_3 == True:
            extra_amount_AL = line[31:38]
            print("line 3 AL:", line, "base mount 3 AL:",base_amount_AL, "numcheck", numcheck, "extra mount 3 AL:",extra_amount_AL )


        if "M" <= line[25:30] <= "Z" and in_block_3 == True and line[25] != "U":
            extra_amount_MZ = line[31:38]
            print("line 3 MZ !=U:", line, "base amount 3 MZ",base_amount_MZ,"numcheck:", numcheck, "extra mount 3 AL",extra_amount_MZ)

        elif "M" <= line[25:30] <= "Z" and in_block_3 == True and line[25] == "U":
            extra_amount_MZ = line[31:38]
            print("line 3 U:", line, "base amount 3 U:",base_amount_U , "numcheck:", numcheck, "extra mount 3 U:",extra_amount_MZ)

        if line[0] =="#":
            in_block_3 = False













