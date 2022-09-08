import re
import sys

text = input()

pattern = r'(#|\|)(?P<name>[a-zA-Z]+|[a-zA-Z\s*]+)\1(?P<date>[0-9]{2}\/[0-9]{2}\/[0-9]{2})\1(?P<calories>\d+)\1'

result = re.finditer(pattern, text)
new_list = []
cal_sum = 0
for each in result:
    new_list.append([each.group(2), each.group(3), each.group(4)])
    cal_sum += int(each.group(4))

days = cal_sum // 2000
print(f"You have food to last you for: {days} days!")
for s in new_list:
    print(f"Item: {s[0]}, Best before: {s[1]}, Nutrition: {s[2]}")


