def possible_cors(matrix, row, col):
    possible_cords = [
        [row - 1, col - 1],
        [row - 1, col],
        [row - 1, col + 1],
        [row, col - 1],
        [row, col + 1],
        [row + 1, col - 1],
        [row + 1, col],
        [row + 1, col + 1]]
    result = []
    for arow, acol in possible_cords:
        if 0 <= arow < len(matrix) and 0 <= acol < len(matrix) and matrix[arow][acol] > 0:
            result.append([arow, acol])
    return result


size = int(input())
matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

coordinates = input().split()
for each in coordinates:
    row, col = [int(x) for x in each.split(',')]
    damage = matrix[row][col]

    if damage <= 0:
        continue

    matrix[row][col] -= damage
    damages = possible_cors(matrix, row, col)
    for x, y in damages:
        matrix[x][y] -= damage

alive_cells = 0
alive_cells_sum = 0

for row in matrix:
    for el in row:
        if el > 0:
            alive_cells += 1
            alive_cells_sum += el

print(f'Alive cells: {alive_cells}')
print(f'Sum: {alive_cells_sum}')
for row in matrix:
    print(*row, sep=' ')
