rows = int(input())

matrix = [[int(x) for x in input().split(' ')]for _ in range(rows)]
primary = []
secondary = []
for index in range(rows):
    primary.append(matrix[index][index])
    secondary.append(matrix[index][rows - 1 - index])

primary_sum = sum(primary)
secondary_sum = sum(secondary)
print(abs(primary_sum - secondary_sum))