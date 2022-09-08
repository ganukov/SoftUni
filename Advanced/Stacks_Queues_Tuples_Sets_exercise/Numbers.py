first = set([int(x) for x in input().split()])
second = set([int(y) for y in input().split()])

number = int(input())

for _ in range(number):
    command = input().split()
    to_do = command[0]
    where = command[1]

    if to_do == 'Add':
        if where == 'First':
            first = first.union([int(x) for x in command[2:]])
        else:
            second = second.union([int(x) for x in command[2:]])
    elif to_do == 'Remove':
        if where == 'First':
            first = first.difference([int(x) for x in command[2:]])
        else:
            second = second.difference([int(x) for x in command[2:]])
    else:
        print(first.issubset(second) or second.issubset(first))


print(*sorted(first), sep=', ')
print(*sorted(second), sep=', ')
