name_actor = input()
academy_points = float(input())
num_judges = int(input())
total_points = 0
points_condition = True
for _ in range(num_judges):
    name_judge = input()
    points_judge = float(input())
    total_points += ((len(name_judge) * points_judge) / 2)

    if total_points >= 1250.5:
        points_condition = False
        break
if points_condition:
    diff = abs(total_points + academy_points - 1250.5)
    print(f"Sorry, {name_actor} you need {diff} more!")
else:
    diff = abs(total_points + academy_points)
    print(f"Congratulations, {name_actor} got a nominee for leading role with {diff}!")


