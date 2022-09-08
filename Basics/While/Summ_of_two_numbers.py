import sys

number = int(input())
number_1 = int(input())
magic_number = int(input())
combination = 0
condition = False
for n in range(number, number_1 + 1):
    for m in range(number, number_1 + 1):
        combination += 1
        if n + m == magic_number:
            condition = True
            print(f"Combination N:{combination} ({n} + {m} = {magic_number})")
            sys.exit()
if not condition:
    print(f"{combination} combinations - neither equals {magic_number}")


