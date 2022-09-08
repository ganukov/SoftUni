number_1 = int(input())
number_2 = int(input())

for numbers in range(number_1,number_2 +1):
    chars = chr(numbers)
    print(f"{chars} ", end="")