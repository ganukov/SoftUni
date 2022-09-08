def fire(warship,index,damage_fire):

    if index in range(len(warship)):
        warship[index] -= damage_fire
        if warship[index] <= 0:
            print(f"You won! The enemy ship has sunken.")
        return warship


def defend(ship,index1,index2,damage):

    if index1 and index2 in range(len(ship)):
        for each in (ship.index(index1),ship.index(index2) +1):
            each -= damage
            if each <= 0:
                print(f"You lost! The pirate ship has sunken.")
            return ship


def repair(ship,index,health):

    if index in range(len(ship)):
        value = ship[index]
        if value < max_capacity:
            value += health
    return ship


def status(ship,count):

    for each in ship:
        if each < (0.8 * max_capacity):
            count += 1
    print(f"{count} sections need repair.")
    return ship


def war(ship,warship):
    command = input()

    while command != "Retire":
        current = command.split()

        if current[0] == "Retire":
            if len(warship) > 0 and len(ship) > 0:
                print(f"Pirate ship status: {sum(ship)}")
                print(f"Warship status: {sum(warship)}")
            break

        if current[0] == "Fire":
            index = int(current[1])
            damage_fire = int(current[2])
            fire(warship,index,damage_fire)

        if current[0] == "Defend":
            index1 = int(current[1])
            index2 = int(current[2])
            damage = int(current[3])
            defend(ship,index1,index2,damage)

        if current[0] == "Repair":
            index = int(current[1])
            health = int(current[2])
            ship = repair(ship,index,health)
        if current[0] == "Status":
            count = 0
            status(ship,count)
        command = input()


status_ship = list(map(int, input().split(">")))
status_war = list(map(int, input().split(">")))
max_capacity = int(input())




