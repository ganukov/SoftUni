points = int(input())
bonus = 0
if points <= 100:
    bonus = 5

elif 100 < points < 1000:
    bonus = 0.2 * points

elif points > 1000:
    bonus = 0.1 * points

if points % 2 == 0:
    bonus += 1
elif points % 10 == 5:
    bonus += 2

all_points = bonus + points
print(bonus)
print(all_points)
