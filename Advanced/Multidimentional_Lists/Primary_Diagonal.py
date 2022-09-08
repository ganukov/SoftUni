size = int(input())

matrix = [
    [int(x) for x in input().split()] for _ in range(size)
]
result = 0
# VERY SLOW
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         if i == j:
#             result += matrix[i][j]
# BETTER # when we know rows == columns
for i in range(len(matrix)):
    result += matrix[i][i]
print(result)