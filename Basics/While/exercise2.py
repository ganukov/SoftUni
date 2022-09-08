import math

balls = int(input())
points = 0
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
other_colors_balls = 0
divide_from_black_balls = 0
for _ in range(0, balls):
    color = input()
    if color == "red":
        points += 5
        red_balls += 1
    elif color == "orange":
        points += 10
        orange_balls += 1
    elif color == "yellow":
        points += 15
        yellow_balls += 1
    elif color == "white":
        points += 20
        white_balls += 1
    elif color == "black":
        points = math.floor(points / 2)
        divide_from_black_balls += 1
    else:
        other_colors_balls += 1

print(f"Total points: {points}")
print(f"Red balls: {red_balls}")
print(f"Orange balls: {orange_balls}")
print(f"Yellow balls: {yellow_balls}")
print(f"White balls: {white_balls}")
print(f"Other colors picked: {other_colors_balls}")
print(f"Divides from black balls: {divide_from_black_balls}")
