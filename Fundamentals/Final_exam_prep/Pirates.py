import sys

cities = {}

while True:
    info = input().split('||')
    if info[0] == "Sail":
        while True:
            command = input().split('=>')
            if command[0] == 'End':
                if len(cities.keys()) > 0:
                    print(f"Ahoy, Captain! There are {len(cities.keys())} wealthy settlements to go to:")
                    for x in cities:
                        print(f"{x} -> Population: {cities[x]['pop']} citizens, Gold: {cities[x]['gold']} kg")
                else:
                    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
                sys.exit()

            new_town = command[1]
            if command[0] == 'Plunder':
                people = int(command[2])
                new_gold = int(command[3])
                cities[new_town]['pop'] -= people
                cities[new_town]['gold'] -= new_gold
                if cities[new_town]['pop'] <= 0:
                    cities.pop(new_town)
                    print(f"{new_town} plundered! {new_gold} gold stolen, {people} citizens killed.")
                    print(f'{new_town} has been wiped off the map!')

                elif cities[new_town]['gold'] <= 0:
                    cities.pop(new_town)
                    print(f"{new_town} plundered! {new_gold} gold stolen, {people} citizens killed.")
                    print(f'{new_town} has been wiped off the map!')
                else:
                    print(f"{new_town} plundered! {new_gold} gold stolen, {people} citizens killed.")
            elif command[0] == 'Prosper':
                gold1 = int(command[2])
                if gold1 <= 0:
                    print(f'Gold added cannot be a negative number!')
                else:
                    cities[new_town]['gold'] += gold1
                    print(f'{gold1} gold added to the city treasury. {new_town} now has {cities[new_town]["gold"]} gold.')

    town = info[0]
    populations = int(info[1])
    gold = int(info[2])

    if town in cities:
        cities[town]['pop'] += populations
        cities[town]['gold'] += gold
    else:
        cities[town] = {'pop': populations, 'gold': gold}