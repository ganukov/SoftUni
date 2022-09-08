from collections import deque

number_pumps = int(input())
pumps = deque()


for _ in range(number_pumps):
    pumps.append([int(x) for x in input().split()])

for attempt in range(number_pumps):
    tank = 0
    failed = False
    for petrol, distance in pumps:
        tank = tank + petrol - distance
        if tank < 0:
            failed = True
            break

    if failed:
        pumps.append(pumps.popleft())
    else:
        print(attempt)
        break
