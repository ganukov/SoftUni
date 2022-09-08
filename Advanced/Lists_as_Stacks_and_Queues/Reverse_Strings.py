t = input()

s = []

for c in t:
    s.append(c)

reversed_string = ""

while s:
    reversed_string += s.pop()

print(reversed_string)
