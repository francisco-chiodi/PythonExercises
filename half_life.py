
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
            continue

        if "A" <= line[25:31] <= "L" and in_block_1 == True:
            base_mount_AL = line[2:7]
            print("line 1 AL", line, base_mount_AL)

        if "M" <= line[25:31] <= "Z" and in_block_1 == True and line[0] != "U":
            base_mount_MZ = line[8:14]
            print("line 1 MZ", line, base_mount_MZ)

        #              BLOCK2
        if line[0:20] == "# 196645252478107261":
            in_block_1 = False
            in_block_2 = True
            continue

        if "A" <= line[25:31] <= "L" and in_block_2 == True:
            base_mount_AL = line[2:7]
            print("line 2 AL", line, base_mount_AL)

        if "M" <= line[25:30] <= "Z" and in_block_2 == True:
            base_mount_MZ = line[8:14]
            print("line 2 MZ", line, base_mount_MZ)

        #              BLOCK3
        if line[0:20] == "# 48500 62953 294690":
            in_block_1 = False
            in_block_2 = False
            in_block_3 = True
            continue


        if "A" <= line[25:31] <= "L" and in_block_3 == True:
            base_mount_AL = line[2:7]
            print("line 3 AL", line, base_mount_AL)


        if "M" <= line[25:31] <= "Z" and in_block_3 == True:
            base_mount_MZ = line[8:14]
            print("line 3 MZ", line, base_mount_MZ)
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