emp_eff1 = int(input())
emp_eff2 = int(input())
emp_eff3 = int(input())
students_count = int(input())
time = 0
students_left = 0
while students_count >= 0:

    all_eff = emp_eff1 + emp_eff2 + emp_eff3
    if time % 4 == 0:
        all_eff = 0

    students_count -= all_eff
    if students_count <= 0:
        break
    time += 1


print(f"Time needed: {time}h.")

