n = int(input())
numbers = list()
filtered = list()

for i in range(n):
    number = int(input())
    numbers.append(number)

command = input()
if command == "even":
    for each_number in numbers:
        if each_number % 2 == 0 or each_number == 0:
            filtered.append(each_number)
elif command == "odd":
    for each_number in numbers:
        if each_number % 2 != 0:
            filtered.append(each_number)
elif command == "positive":
    for each_number in numbers:
        if each_number >= 0:
            filtered.append(each_number)
elif command == "negative":
    for each_number in numbers:
        if each_number < 0 :
            filtered.append(each_number)

print(filtered)
