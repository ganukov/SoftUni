number_of_balls = int(input())
max_value = 0
weight_1 = 0
speed_1 = 0
quality_1 = 0

for each_ball in range(1, number_of_balls + 1):

    weight = int(input())
    speed = int(input())
    quality = int(input())
    value = (weight / speed) ** quality
    if value > max_value:
        max_value = int(value)
        weight_1 = int(weight)
        speed_1 = int(speed)
        quality_1 = int(quality)
print(f"{weight_1} : {speed_1} = {max_value} ({quality_1})")
