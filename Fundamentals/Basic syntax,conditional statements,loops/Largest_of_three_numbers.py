import sys

num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

max_num = -sys.maxsize

if num_1 > num_2 and num_1 > num_3 :
    max_num = num_1
elif num_2 > num_1 and num_2 > num_3:
    max_num = num_2
elif num_3 > num_2 and num_3 > num_1:
    max_num = num_3

print(max_num)