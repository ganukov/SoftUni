rows = int(input())
# matrix = []
#
# for _ in range(rows):
#     el = [int(x) for x in input().split(', ')]
#     matrix.append(
#         [x for x in el if x % 2 == 0]
#     )
#
# print(matrix)

matrix = [[int(x) for x in (input().split(', '))]for _ in range(rows)]

print([[x for x in row if x % 2 == 0] for row in matrix])