def get_number_of_steps(number):
    number_list = range(1, number, 2)
    for i in number_list:
        if number / (i+2)**2 > 0 & number // (i+4)**2 == 0:
            steps = i
    return steps

def get_number_of_jumps(number):
   find_number_in_row = get_number_of_steps(number)+2  # type: int
   find_middle = int(round(float(find_number_in_row) / 2))
   find_position = number % find_middle
   return find_position

def total_number_of_steps(number):
    return get_number_of_steps(number) + get_number_of_jumps(number)

if __name__ == "__main__":
    assert total_number_of_steps(9) == 2
    assert total_number_of_steps(25) == 5
    assert total_number_of_steps(26) == 6
    print("hi")
