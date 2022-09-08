size = int(input())

matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

while True:
    info = input().split()
    command = info[0]
    if command == 'END':
        for row in matrix:
            print(*row,sep=' ')
        break
    row = int(info[1])
    col = int(info[2])
    value = int(info[3])
    if command == 'Add' and 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
        matrix[row][col] += value
    elif command == 'Subtract' and 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
        matrix[row][col] -= value
    else:
        print('Invalid coordinates')

