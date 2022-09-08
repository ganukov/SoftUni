import re

participants = input().split(',')
winners = {'name': [],'points': []}


while True:
    command = input()

    if command == "end of race":
        break
    for each in command:
        for i in each:
            if i.isdigit():
                digits.append(i)
            elif i.isalpha():
                names.append(i)

    print(names,digits)
