rows = int(input())

matrix = [[int(x) for x in input().split(', ')]for _ in range(rows)]
primary = []
secondary = []
for index in range(rows):
    primary.append(matrix[index][index])
    secondary.append(matrix[index][rows - 1 - index])
print(f'Primary diagonal: {", ".join([str(x) for x in primary])}. Sum: {sum(primary)}')
print(f'Secondary diagonal: {", ".join([str(x) for x in secondary])}. Sum: {sum(secondary)}')
