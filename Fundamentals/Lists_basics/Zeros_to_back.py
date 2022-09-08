info = input().split(",")
numbers = []
zeros = []

for num in info:
    if int(num) == 0:
        zeros.append(int(num))
    else:
        numbers.append(int(num))
print(numbers + zeros)

