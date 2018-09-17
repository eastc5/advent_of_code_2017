def get_number_of_cycles(number):
    number_list = range(1, number, 2)
    for i in number_list:
        if number / i**2 > 0 & number // (i+2)**2 == 0:
            circle = i
    return circle
