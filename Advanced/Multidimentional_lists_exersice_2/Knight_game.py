def next_move(matrix, row, col):
    possible_kill = [
        [row - 2, col - 1],
        [row - 2, col + 1],
        [row - 1, col - 2],
        [row - 1, col + 2],
        [row + 1, col - 2],
        [row + 1, col + 2],
        [row + 2, col - 1],
        [row + 2, col + 1]
    ]
    result = 0
    for child_row, child_col in possible_kill:
        if 0 <= child_row < len(matrix) and 0 <= child_col < len(matrix) and matrix[child_row][child_col] == 'K':
            result += 1
    return result


size = int(input())
matrix = []

for _ in range(size):
    matrix.append(list(input()))

removed_knights = 0

while True:
    best_count = 0
    knight_row = 0
    knight_col = 0
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == '0':
                continue
            count = next_move(matrix, row, col)
            if count > best_count:
                best_count = count
                knight_row = row
                knight_col = col

    if best_count == 0:
        break

    matrix[knight_row][knight_col] = '0'
    removed_knights += 1

print(removed_knights)
