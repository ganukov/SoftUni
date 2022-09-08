import re
import sys

num = int(input())

for each in range(num):
    text = input()

    pattern = r"\!\b([A-Z]{1}[a-z]{3,})\b\!\:\[{1}\b([A-Za-z]{8,})\b\]{1}"
    matches1 = re.findall(pattern,text)
    matches = re.finditer(pattern,text)

    if len(matches1) == 0:
        print(f"The message is invalid")
    else:
        for match in matches:
            nums = []
            for i in match.group(2):
                nums.append(ord(i))
            print(f"{match.group(1)}: {' '.join([str(x) for x in nums])}")






