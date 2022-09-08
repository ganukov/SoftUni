import sys

num_1 = int(input())
num_2 = int(input())
num_3 = int(input())


def solve(num_1, num_2, num_3):
    result = min(num_1,num_2,num_3)
    return result


print(solve(num_1, num_2, num_3))