import math
count_tour = int(input())
count_points = int(input())
total_points = 0
winning_rate = 0
for _ in range(count_tour):
    grade = (input())
    if grade.upper() == "W":
        total_points += 2000
        winning_rate += 1
    elif grade.upper() == "F":
        total_points += 1200
    elif grade.upper() == "SF":
        total_points += 720


total_points += count_points
mediocre_points = (total_points - count_points) / count_tour
winning_rate = winning_rate / count_tour * 100
print(f"Final points: {total_points}")
print(f"Average points: {math.floor(mediocre_points)}")
print(f"{winning_rate:.2f}%")
