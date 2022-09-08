number_tab = int(input())
salary = int(input())
salary_condition = True
for _ in range(number_tab):
    name_web = input()
    if name_web == "Facebook":
        salary -= 150
    elif name_web == "Instagram":
        salary -= 100
    elif name_web == "Reddit":
        salary -= 50

    if salary <= 0:
        salary_condition = False
        break

if salary_condition:
    print(salary)
else:
    print(f"You have lost your salary.")

