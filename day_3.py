def get_number_of_steps(number):
    number_list = [x for x in range(number+1) if x % 2 == 1]
    for i,value in enumerate(number_list):
        if number <= (value)**2:
            return i

def get_number_of_jumps(number):
    if number == 1:
        return  0
    ring_number = get_number_of_steps(number)

    ring_lengths = [x for x in range(number+1) if x % 2 == 1]

    largest_number_in_ring = (ring_lengths[ring_number])**2

    inner_ring_largest_number = ring_lengths[ring_number - 1]**2

    lenght_of_current_ring = largest_number_in_ring -inner_ring_largest_number

    distance_between_middles= int(lenght_of_current_ring/4)

    starting_point = int(largest_number_in_ring - distance_between_middles / 2)

    middle_points = range(starting_point, inner_ring_largest_number,-distance_between_middles)

    find_position = min([abs(x - number) for x in middle_points])

    return find_position

def total_number_of_steps(number):
    return get_number_of_steps(number) + get_number_of_jumps(number)

if __name__ == "__main__":
    assert total_number_of_steps(1) == 0
    assert total_number_of_steps(26) == 5
    assert total_number_of_steps(12) == 3
    assert total_number_of_steps(1024) == 31
    print("hi")
    print(total_number_of_steps(265149))
