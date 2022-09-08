number_of_lines = int(input())

tank_capacity = 255
volume = 0
for each_line in range(number_of_lines):
    litters = int(input())
    volume += litters

    if volume > 255:
        volume -= litters
        print(f"Insufficient capacity!")
        continue

print(volume)