import sys

divisor = int(input())
boundary = int(input())
largest_number = -sys.maxsize

for n in range(divisor, boundary + 1):
    if n % divisor == 0 and n <= boundary:
        largest_number = n
print(largest_number)
