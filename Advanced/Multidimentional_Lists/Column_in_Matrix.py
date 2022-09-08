# import sys
#
# size = int(input())
#
# matrix = [
#     [x for x in input()] for _ in range(size)
# ]
# condition = False
# what = input()
# for x in matrix:
#     for y in x:
#         if y == what:
#             print(f'({matrix.index(x)}, {x.index(y)})')
#             sys.exit()
#
# if not condition:
#     print(f'{what} does not occur in the matrix')
import sys
from io import StringIO

test_input1 = '''3
ABC
DEF
X!@
!'''

sys.stdin = StringIO(test_input1)
n = int(input())

matrix = [list(input()) for _ in range(n)]
symbol = input()
is_found = False
for row_index in range(n):
    for column_index in range(n):
        if matrix[row_index][column_index] == symbol:
            print(f'({row_index}, {column_index})')
            sys.exit()

if not is_found:
    print(f'{symbol} does not occur in the matrix')