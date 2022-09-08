import re

text = input()

matches = re.finditer(r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.[0-9]+)?($|(?=\s))", text)

for match in matches:
    print(match.group(), end=" ")