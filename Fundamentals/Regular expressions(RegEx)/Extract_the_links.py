import re

while True:
    text = input()

    if not text:
        break

    pattern = r"w{3}\.[A-Za-z0-9\-]+(\.[a-z]+){1,}"
    matches = re.finditer(pattern, text, re.MULTILINE)

    for match in matches:
        print(match.group())
