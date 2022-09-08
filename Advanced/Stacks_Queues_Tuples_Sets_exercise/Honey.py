from collections import deque

bees = deque([int(x) for x in input().split()])
nectars = [int(x) for x in input().split()]
symbols = input().split()
operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
}
total_honey = 0

while bees and nectars:
    bee = bees.popleft()
    nectar = nectars.pop()
    if bee > nectar:
        bees.appendleft(bee)
    elif nectar == 0:
        continue
    else:
        for ch in symbols:
            if ch in '+-*/':
                total_honey += abs(operations[ch](bee,nectar))
                symbols.remove(ch)
                break


print(f'Total honey made: {total_honey}')
if bees:
    print(f'Bees left: {", ".join([str(x) for x in bees])}')
if nectars:
    print(f'Nectar left: {", ".join([str(x) for x in nectars])}')