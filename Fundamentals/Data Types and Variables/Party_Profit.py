group_size = int(input())
days = int(input())
profit = 0

for each_day in range(1, days + 1):

    if each_day % 10 == 0:
        group_size -= 2
    if each_day % 15 == 0:
        group_size += 5
    profit += 50 - (group_size * 2)
    if each_day % 3 == 0:
        profit -= 3*group_size
    if each_day % 5 == 0:
        profit += 20*group_size
        if each_day % 3 == 0:
            profit -= 2 * group_size
print(f"{group_size} companions received {int(profit / group_size)} coins each.")

