def possible_moves(field, row, col):
    positions = [
        [row + 1, col], [row - 1, col], [row, col + 1], [row, col - 1],
        [row + 2, col], [row - 2, col], [row, col + 2], [row, col - 2],
        [row + 3, col], [row - 3, col], [row, col + 3], [row, col - 3],
        [row + 4, col], [row - 4, col], [row, col + 4], [row, col - 4]
    ]
    result = []
    for r, c in positions:
        if 0 <= r < len(field) and 0 <= c < len(field) and field[r][c] != 'X':
            result.append([r, c])
    return result


size = int(input())

field = []

for _ in range(size):
    field.append(input())

bunny_row = 0
bunny_col = 0
positions = {
    'down': [],
    'up': [],
    'right': [],
    'left': []
}

for row in range(size):
    for col in range(size):
        if field[row][col] == 'B':
            bunny_row = row
            bunny_col = col
