def get_children(row, col, rows, columns):
    possible_children = [
        [row - 1, col],
        [row, col - 1],
        [row, col + 1],
        [row + 1, col]
    ]
    result = []
    for child_row, child_col in possible_children:
        if not is_outside(child_row, child_col, rows, columns):
            result.append([child_row, child_col])

    return result


def is_outside(row, col, rows, columns):
    return row < 0 or col < 0 or row >= rows or col >= columns


def get_next_pos(start_row, start_col, each):
    if each == 'U':
        return start_row - 1, start_col
    if each == 'D':
        return start_row + 1, start_col
    if each == 'L':
        return start_row, start_col - 1
    if each == 'R':
        return start_row, start_col + 1


rows, columns = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    column = input().split()
    for each in column:
        matrix.append(list(each))

directions = input()
dirs = []
start_row = 0
start_col = 0
bunny_dir = set()

for row in matrix:
    current_row = matrix.index(row)
    for col in row:
        current_col = row.index(col)
        if col == 'P':
            start_idx = [current_row, current_col]
            start_row, start_col = [int(x) for x in start_idx]
            matrix[start_row][start_col] = '.'
        elif col == 'B':
            bunny_dir.add(f'{current_row} {current_col}')

won = False
dead = False

for each in directions:
    next_row, next_col = get_next_pos(start_row, start_col, each)
    matrix[start_row][start_col] = '.'
    if is_outside(next_row, next_col, start_row, start_col):
        won = True
    elif matrix[next_row][next_col] == 'B':
        dead = True
        start_row, start_col = next_row, next_col
    else:
        matrix[next_row][next_col] = 'P'

    new_bunnies = set()

    for bunny in bunny_dir:
        bunny_row, bunny_col = [int(x) for x in bunny.split()]
        children = get_children(bunny_row, bunny_col, rows, columns)
        for child_row, child_col in children:
            new_bunnies.add(f'{child_row} {child_col}')
            matrix[child_row][child_col] = 'B'
            if child_row == start_row and child_col == start_col:
                dead = True
    bunny_dir = bunny_dir.union(new_bunnies)

    if won or dead:
        break

for row in matrix:
    print(*row, sep='')
if won:
    print(f'won: {start_row} {start_col}')
else:
    print(f'dead: {start_row} {start_col}')
