from collections import deque
d = deque()

operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b,
}
exp = input().split()
for ch in exp:
    if ch in '+-*/':
        while len(d) > 1:
            left = d.popleft()
            right = d.popleft()
            result = operations[ch](left, right)
            d.appendleft(result)
    else:
        d.append(int(ch))

print(*d)