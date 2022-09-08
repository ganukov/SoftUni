from collections import deque

cars = deque()
parts = deque()

green = int(input())
free_window = int(input())
green_light = green
window = free_window
while True:
    command = input()
    if command == 'END':
        print('Everyone is safe.')
        print(f'{len(cars)} total cars passed the crossroads.')
        break
    elif command == 'green':
        green_light = green
        window = free_window
    else:
        current_car = command
        if green_light > 0:
            for each in current_car:
                parts.append(each)
            for i in range(green_light):
                if parts:
                    parts.popleft()
                    green_light -= 1
            if not parts:
                cars.append(current_car)
            if green_light == 0 and parts:
                while window > 0:
                    window -= 1
                    parts.popleft()
                    if not parts:
                        break
                if window <= 0 and parts:
                    print(f"A crash happened!")
                    print(f"{current_car} was hit at {parts.popleft()}.")
                    break
                else:
                    cars.append(current_car)

