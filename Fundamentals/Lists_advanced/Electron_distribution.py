def electron_distribution(number_of_electrons):
    shelves_filled = []
    position = 0

    while number_of_electrons > 0:
        position += 1
        max_filled = 2*(position**2)
        if max_filled > number_of_electrons:
            max_filled = number_of_electrons
        number_of_electrons -= max_filled
        shelves_filled.append(max_filled)
    print(shelves_filled)


electrons = int(input())
electron_distribution(electrons)
