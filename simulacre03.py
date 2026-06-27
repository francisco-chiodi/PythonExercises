def digit(char):
    return "0" <= char <= "9"


def minus(char):
    return "a" <= char <= "z" or char in "áéíóúüñ"


def cons(char):
    return char.lower() in "bcdfghijklmnñpqrstvwxyz"


def principal():
    m = open("entrada.txt", encoding="utf-8")
    text = m.read() + " "
    m.close()

    count_condition = count_digit = count_char = count_n = count_p4 = count_p3 = 0
    last_char = ""
    minus_all = True
    has_a = False
    start_se = True
    letter = None

    for char in text:
        if char != " " and char != ".":  # inside word
            count_char += 1
            last_char = char

            if count_char == 1 and char not in "sS":
                start_se = False
            if count_char == 2 and char not in "eE":
                start_se = False

            if char in "nN":
                count_n += 1

            if char in "aA" and count_char <= 4:
                has_a = True

            if digit(char):
                count_digit += 1

            if not minus(char) and not digit(char):
                minus_all = False

        else:  # outside word
            # CONTROL CRÍTICO: Solo evaluamos si realmente procesamos una palabra
            if count_char > 0:

                # Punto 2
                if count_digit >= 1:
                    if letter is None or count_char < letter:
                        letter = count_char

                # Punto 1
                if count_digit == 1 and minus_all == True:
                    count_condition += 1

                # Punto 3
                if count_n == 2 and has_a:
                    count_p3 += 1

                # Punto 4
                if start_se and count_char >= 2 and cons(last_char):
                    count_p4 += 1

            # RESETS (Siempre se resetea todo, haya o no palabra)
            count_digit = 0
            count_char = 0
            count_n = 0
            has_a = False
            start_se = True
            minus_all = True
            last_char = ""

    print("the first condition is met by:", count_condition)
    print("shortest word with a number is:", letter)
    print("3 is:", count_p3)
    print("4 is:", count_p4)


if __name__ == "__main__":
    principal()