rows = int(input())
matrix = []

for _ in range(rows):
    el = [int(x) for x in input().split(', ')]
    matrix.append(el)

print([
    v
    for row in matrix
    for v in row
])