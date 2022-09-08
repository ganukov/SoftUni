allowed_q_each_type = int(input())
days_left_until_C = int(input())
budget = 0
cr_spirit = 0


for each_day in range(1, days_left_until_C + 1):
    if each_day % 11 == 0:
        allowed_q_each_type += 2
    if each_day % 2 == 0:
        budget += allowed_q_each_type * 2
        cr_spirit += 5
    if each_day % 3 == 0:
        budget += (allowed_q_each_type * 5) + (allowed_q_each_type * 3)
        cr_spirit += 13
    if each_day % 5 == 0:
        budget += allowed_q_each_type * 15
        cr_spirit += 17
        if each_day % 3 == 0:
            cr_spirit += 30
    if each_day % 10 == 0:
        budget += 23
        cr_spirit -= 20


if days_left_until_C % 10 == 0:
    cr_spirit -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {cr_spirit}")

