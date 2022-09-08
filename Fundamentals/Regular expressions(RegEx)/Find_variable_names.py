import re

text = input()
matches = re.findall(r"\b_[a-zA-Z0-9]+\b",text)

result = list()

for match in matches:
    result.append(match[1:])

print(",".join(result))