from collections import deque

chocolates = [int(x) for x in input().split(', ')]
cups_of_milk = deque([int(x) for x in input().split(', ')])
shakes = 0

while chocolates and cups_of_milk and shakes < 5:

    current_choc = chocolates.pop()
    current_cup = cups_of_milk.popleft()

    if current_choc <= 0 and current_cup <= 0:
        continue
    if current_choc <= 0:
        cups_of_milk.appendleft(current_cup)
        continue
    if current_cup <= 0:
        chocolates.append(current_choc)
        continue
    if current_choc == current_cup:
        shakes += 1
    else:
        cups_of_milk.append(current_cup)
        chocolates.append(current_choc - 5)
if shakes == 5:
    print(f'Great! You made all the chocolate milkshakes needed!')
else:
    print(f'Not enough milkshakes.')
if chocolates:
    print(f'Chocolate: {", ".join([str(x) for x in chocolates])}')
else:
    print(f'Chocolate: empty')
if cups_of_milk:
    print(f'Milk: {", ".join([str(x) for x in cups_of_milk])}')
else:
    print(f'Milk: empty')



