import sys

happy = list(map(int, input().split()))
happy_imp = int(input())

average = (sum(happy) / len(happy)) * happy_imp
happy_emp = []
for x in happy:
    if x * happy_imp >= average:
        happy_emp.append(x)

if len(happy_emp) >= len(happy) / 2:

    print(f"Score: {len(happy_emp)}/{len(happy)}. Employees are happy!")
    sys.exit()
else:
    print(f"Score: {len(happy_emp)}/{len(happy)}. Employees are not happy!")
    sys.exit()