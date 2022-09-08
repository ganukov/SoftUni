rows, columns = [int(x) for x in input().split(' ')]
matrix = []

for row in range(rows):
    sub_matrix = []
    for col in range(columns):
        first_letter = (chr(ord('`') + row + 1)) + (chr(ord('`') + col + row + 1)) + (chr(ord('`') + row + 1))
        sub_matrix.append(first_letter)
    matrix.append(sub_matrix)

for each in matrix:
    print(f'{" ".join([str(x) for x in each])}')