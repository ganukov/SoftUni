import re

text = input()
word = input()

matches = rf'\b{word}\b'
result = re.findall(matches,text,re.IGNORECASE)
print(len(result))