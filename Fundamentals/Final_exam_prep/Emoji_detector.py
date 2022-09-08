import re
import math
text = input()
pattern = r"(\:\:|\*\*)([A-Za-z]{3,})\1"
matches = re.finditer(pattern,text)
nums = []
count = 0

for i in text:
    if i.isdigit():
        nums.append(int(i))

limit = math.prod(nums)
asd = []
for match in matches:
    count += 1
    asd.append(match[0])
    sum_all = []
    for s in match.group(2):
        sum_all.append(ord(s))
print(f"Cool threshold: {limit}")
print(f"{count} emojis found in the text. The cool ones are:")
for y in asd:
    print(f"{y}")