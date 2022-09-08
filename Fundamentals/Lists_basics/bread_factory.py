import sys

events = input().split("|")
current_energy = 100
current_coins = 100

condition = False
for event in events:
    current_event_elements = event.split("-")
    name = current_event_elements[0]
    number = int(current_event_elements[1])
    gained_energy = 0
    gained_coins = 0
    if name == "rest":
        gained_energy += number
        current_energy += gained_energy
        if current_energy > 100:
            current_energy = 100
            gained_energy = 0
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {current_energy}.")

    elif name == "order":

        if current_energy >= 30:
            gained_coins += number
            current_coins += gained_coins
            current_energy -= 30
            print(f"You earned {gained_coins} coins.")
            condition = True
        else:
            current_energy += 50
            print(f"You had to rest!")

    else:
        if current_coins >= number:
            current_coins -= number
            print(f"You bought {name}.")
            condition = True
        else:
            print(f"Closed! Cannot afford {name}.")

            sys.exit()
if condition:
    print(f"Day completed!")
    print(f"Coins: {current_coins}")
    print(f"Energy: {current_energy}")