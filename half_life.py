
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
            print("line 1 AL", line, "base mount 1 AL",base_amount_AL, "extra mount 1 AL",extra_amount_AL)


        if "M" <= line[25:30] <= "Z" and in_block_1 == True and line[0] != "U":
            extra_amount_MZ = line[31:38]
            print("line 1 MZ", line, "base mount 1 MZ",base_amount_MZ, "extra mount 1 MZ",extra_amount_MZ , "numcheck", numcheck)
            #total_1 = base_mount_MZ + extra_mount_AL
        elif "M" <= line[25:30] <= "Z" and in_block_1 == True and line[0] == "U":
            print("line 3 U", line, "base mount 3 AL",base_amount_U , "numcheck", numcheck)


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


            print("line 2 AL", line, "base mount 2 AL",base_amount_AL, "extra mount 2 AL",extra_amount_AL, "numcheck", numcheck)

        if "M" <= line[25:30] <= "Z" and in_block_2 == True and line[25] != "U":
            extra_amount_MZ = line[31:38]
            print("line 2 MZ", line, "base mount 2 MZ",base_amount_MZ, "extra mount 2 AL",extra_amount_MZ , "numcheck", numcheck)

        elif "M" <= line[25:30] <= "Z" and in_block_2 == True and line[25] == "U":
            print("THIS IS U", line)


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
            print("line 3 AL", line, "base mount 3 AL",base_amount_AL, "extra mount 3 AL",extra_amount_AL , "numcheck", numcheck)


        if "M" <= line[25:30] <= "Z" and in_block_3 == True and line[25] != "U":
            extra_amount_MZ = line[31:38]
            print("line 3 MZ", line, "base mount 3 MZ",base_amount_MZ, "extra mount 3 AL",extra_amount_MZ , "numcheck", numcheck)

        elif "M" <= line[25:30] <= "Z" and in_block_3 == True and line[25] == "U":
            amount_U = base_amount_U
            print("THIS IS U", line, base_amount_U, "numcheck" , numcheck)

        elif "#" in line[0]:
            in_block_3 = False



        """
                  if line[0: 7] == "# 29664":
                      in_block = True
                      continue
                  if line[0:7] == "# 29664":
                      in_block = False
                      continue  #this ignores current input and forces to jump to the top of the code until the condition is meet.

                      """










        #print(descriptive_letter) #jijo
    print("r1", treatments)
    print("r2", counter_r2)
    print("r3", counter_r3)
    print("r4", counter_r4)
    print("r4", counter_r5)
    print("r4", counter_r6)

"""
""
with open("tratamientos.txt" , "r") as file:

    treatments = 0
    counter_r2 = 0
    counter_r3 = 0
    counter_r4 = 0
    counter_r5 = 0
    counter_r6 = 0





    for line in file:
        treatments += 1

        if  len(line) >= 26:

            descriptive_letter = line[25]

            if descriptive_letter == "A":
                counter_r2 += 1
            elif descriptive_letter == "B":
                counter_r3 += 1
            elif descriptive_letter == "C":
                counter_r4 += 1
            elif descriptive_letter == "D":
                counter_r5 +=1
            elif descriptive_letter =="P":
                counter_r6 +=1


            #print(descriptive_letter) #jijo
    print("r1", treatments)
    print("r2", counter_r2)
    print("r3", counter_r3)
    print("r4", counter_r4)
    print("r4", counter_r5)
    print("r4", counter_r6)




            #print(line)


"""



            #print(line)