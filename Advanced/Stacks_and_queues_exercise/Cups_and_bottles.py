from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = ([int(y) for y in input().split()])

wasted = 0
while cups:
    if not bottles:
        break
    current_cup = cups[0]
    current_bottle = bottles[-1]

    if current_cup <= 0:
        cups.popleft()
    elif current_cup > current_bottle:
        current_cup -= current_bottle
        while current_cup > 0:
            bottles.pop()
            current_bottle = bottles[-1]
            if current_bottle > current_cup:
                wasted += current_bottle - current_cup
            current_cup -= current_bottle

            if current_cup <= 0:
                cups.popleft()
                bottles.pop()
    elif current_bottle >= current_cup:
        current_bottle -= current_cup
        wasted += current_bottle
        cups.popleft()
        bottles.pop()
if not cups:
    if bottles:
        print(f"Bottles: {' '.join(str(i) for i in bottles)}")
if not bottles:
    if cups:
        print(f"Cups: {' '.join(str(i) for i in cups)}")
print(f'Wasted litters of water: {wasted}')




