import sys

n = int(input())
sum_num = 0
max_num = -sys.maxsize

for number in range(0, n):
    num = int(input())
    if num > max_num:
        max_num = num
    sum_num = num + sum_num

if max_num == sum_num - max_num:
    print(f"Yes")
    print(f"Sum = {sum_num - max_num}")
else:
    print(f"No")
    print(f"Diff = {abs(max_num - (sum_num - max_num))}")
