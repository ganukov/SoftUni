import re

info = input()
asd = []
points = 0
pattern = r"(=|/)([A-Z][A-Za-z]{2,})\1"
valid = re.finditer(pattern,info)

for x in valid:
    points += len(x.group(2))
    asd.append(x.group(2))


print(f'Destinations: {", ".join(asd)}')
print(f'Travel Points: {points}')