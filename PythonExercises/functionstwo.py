
def control():
    value = int(input("insert the height: "))
    while value <= 0:
        print("height cant be negative")
        value = int(input("insert the height: "))
    return value


def average(counter, add):
    return (add//counter)



def compare(heights_array, r2, counter_two, counter_three):
    for i in heights_array:
        if i > r2:
            counter_two += 1
        elif i <= r2:
            counter_three += 1
    return counter_two , counter_three #thiss creates a tuple