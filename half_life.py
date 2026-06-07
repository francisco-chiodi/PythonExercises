"""
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


def range_AL(letter):
    if L <= letter <= A:
        print("AL")
    return range


in_block = False

with open("tratamientos.txt" , "r") as file:


    treatments = 0
    counter_r2 = 0
    counter_r3 = 0
    counter_r4 = 0
    counter_r5 = 0
    counter_r6 = 0



    with open("tratamientos.txt", "r") as file:

        treatments = 0
        counter_r2 = 0
        counter_r3 = 0
        counter_r4 = 0
        counter_r5 = 0
        counter_r6 = 0
        in_block = False
        in_block_2 = False

        for line in file:
            treatments += 1

            if line[0:7] == "# 29664":
                in_block = True
                continue
             # this ignores current input and forces to jump to the top of the code until the condition is meet.

            if "A" <= line <= "L" and in_block == True:
                 print(line)



            if line[0:7] == "# 19664":
                in_block_2 = True
                continue
            if "A" <= line <= "L" and in_block == True:
                    print("line2",line)

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




            #print(line)