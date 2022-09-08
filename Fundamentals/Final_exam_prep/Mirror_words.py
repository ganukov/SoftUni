import re
text = input()
match = 0
words = {}
pattern_first = r"(\#|\@)([a-zA-Z]{3,})\1\1([A-Za-z]{3,})\1"
matches = re.finditer(pattern_first,text)
for each in matches:
    match += 1
    if each.group(2) == each.group(3)[::-1]:
        words[each.group(2)] = each.group(3)


if match > 0:
    print(f"{match} word pairs found!")
else:
    print(f'No word pairs found!')
if len(words) <= 0:
    print(f'No mirror words!')
else:
    print(f'The mirror words are:')

print(", ".join([x + " <=> " + str(words[x]) for x in words.keys()]))