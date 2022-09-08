import re

while True:

    text = input()
    if not text:
        break

    matches = re.findall(r"\d+", text)
    if len(matches) > 0:
        print(' '.join(matches), end=" ")
