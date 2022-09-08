import sys


def is_outside(start_row, start_col):
    return start_row < 0 or start_col < 0 or start_row >= len(matrix) or start_col >= len(matrix[0])


size = int(input())
matrix = []
commands = input().split()

for _ in range(size):
    matrix.append([x for x in input().split()])
coal = 0
start_row = 0
start_col = 0
for row in matrix:
    current_row = matrix.index(row)
    for el in row:
        current_col = row.index(el)
        if el == 'c':
            coal += 1
        if el == 's':
            star_idx = [current_row, current_col]
            start_row, start_col = [int(x) for x in star_idx]

for command in commands:
    if command == 'up':
        start_row -= 1
        if 0 <= start_row < len(matrix):
            if matrix[start_row][start_col] == 'c':
                matrix[start_row][start_col] = '*'
                coal -= 1
            elif matrix[start_row][start_col] == 'e':
                print(f'Game over! ({start_row}, {start_col})')
                sys.exit()
        else:
            start_row += 1
    elif command == 'down':
        start_row += 1
        if 0 <= start_row < len(matrix):
            if matrix[start_row][start_col] == 'c':
                matrix[start_row][start_col] = '*'
                coal -= 1
            elif matrix[start_row][start_col] == 'e':
                print(f'Game over! ({start_row}, {start_col})')
                sys.exit()
        else:
            start_row -= 1
    elif command == 'left':
        start_col -= 1
        if 0 <= start_col < len(matrix[0]):
            if matrix[start_row][start_col] == 'c':
                matrix[start_row][start_col] = '*'
                coal -= 1
            elif matrix[start_row][start_col] == 'e':
                print(f'Game over! ({start_row}, {start_col})')
                sys.exit()
        else:
            start_col += 1
    elif command == 'right':

        start_col += 1
        if 0 <= start_col < len(matrix[0]):
            if matrix[start_row][start_col] == 'c':
                matrix[start_row][start_col] = '*'
                coal -= 1
            elif matrix[start_row][start_col] == 'e':
                print(f'Game over! ({start_row}, {start_col})')
                sys.exit()
        else:
            start_col -= 1
if coal == 0:
    print(f"You collected all coal! ({start_row}, {start_col})")
    sys.exit()
else:
    print(f"{coal} pieces of coal left. ({start_row}, {start_col})")
    sys.exit()
