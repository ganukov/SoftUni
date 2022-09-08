n = int(input())
combinations = 0

for t in range(0, n + 1):
    for m in range(0, n + 1):
        for s in range(0, n + 1):
            if t + m + s == n:
                combinations += 1
print(combinations)

