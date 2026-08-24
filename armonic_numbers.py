number = input("input the number: ")
numberlen = str(number)
checknlen = len(number)
justify = 0

if checknlen > 6 or checknlen < 6:
    print("Número no válido para este desafío")
else:

    sum_1 = int(number[0]) + int(number[1]) + int(number[2])
    sum_2 = int(number[3]) + int(number[4]) + int(number[5])
    pi_1 = str(number)[5] + str(number)[4] + str(number[3]) + str(number[2]) + str(number[1]) + str(number[0])

    harmonic = abs(int(number) - int(pi_1))
    harmonic_str = str(harmonic)
    lencheck = len(harmonic_str)

    if lencheck < 6 or lencheck > 6:

        justify = harmonic_str.rjust(6, "0")
        harmonic_str = justify

    sum_harm_1 = int(harmonic_str[0]) + int(harmonic_str[1]) + int(harmonic_str[2])
    sum_harm_2 = int(harmonic_str[3]) + int(harmonic_str[4]) + int(harmonic_str[5])

    if sum_1 == sum_2 and sum_harm_1 == sum_harm_2:
        print('Equilibrado Armónico')
    elif sum_1 == sum_2:
        print('Equilibrado Balanceado')
    else:
        print('Inestable')




