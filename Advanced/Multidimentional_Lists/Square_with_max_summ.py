rows, columns = [int(x) for x in input().split(', ')]
matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]
sub_matrix = []
for row in range(rows - 1):
    for col in range(columns - 1):
        sub_matrix.append([matrix[row][col], matrix[row][col+1], matrix[row + 1][col],
        matrix[row + 1][col + 1]])

total = 0
for i in sub_matrix:
    if sum(i) > total:
        total = sum(i)

for each in sub_matrix:
    if sum(each) == total:
        print(f'{" ".join([str(x) for x in each[0:2]])}')
        print(f'{" ".join([str(x) for x in each[2:4]])}')
        print(total)
