numbers = list(map(int, input().split(", ")))
evens = []
for x in range(len(numbers)):
    if numbers[x] % 2 == 0:
        evens.append(x)

print(evens)
