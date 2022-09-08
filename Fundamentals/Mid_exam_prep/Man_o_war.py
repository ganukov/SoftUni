import sys
status_ship = list(map(int, input().split(">")))
status_war = list(map(int, input().split(">")))
max_capacity = int(input())
count = 0

command = input()

while True:
    current = command.split()

    if current[0] == "Retire":
        if len(status_war) > 0 and len(status_ship) > 0:
            print(f"Pirate ship status: {sum(status_ship)}")
            print(f"Warship status: {sum(status_war)}")
            sys.exit()

    if current[0] == "Fire":
        index_fire = int(current[1])
        damage_fire = int(current[2])

        if index_fire in range(len(status_war)):
            status_war[index_fire] -= damage_fire
            for s in status_war:
                if s <= 0:
                    print(f"You won! The enemy ship has sunken.")
                    sys.exit()

    if current[0] == "Defend":
        index1 = int(current[1])
        index2 = int(current[2])
        damage = int(current[3])

        if 0 <= index1 < len(status_ship) and 0 <= index2 < len(status_ship):
            for i,value in enumerate(status_ship[index1:index2 +1]):
                current_s = value
                value -= damage
                status_ship.insert(i,value)
                status_ship.remove(current_s)
            for i in status_ship:
                if i <= 0:
                    print(f"You lost! The pirate ship has sunken.")
                    sys.exit()

    if current[0] == "Repair":
        index = int(current[1])
        health = int(current[2])
        if index in range(len(status_ship)):
            if status_ship[index] < max_capacity:
                status_ship[index] += health

    if current[0] == "Status":
        for each in status_ship:
            if each < (0.2 * max_capacity):
                count += 1
        print(f"{count} sections need repair.")
    command = input()




