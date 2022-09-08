number = int(input())
garden = {}

for each_plant in range(number):
    plant_info = input().split('<->')
    plant = plant_info[0]
    rarity = int(plant_info[1])
    rating = []
    garden[plant] = rarity,rating

while True:
    command = input().split(' ')
    if '-' in command:
        command.remove('-')
    if command[0] == 'Exhibition':
        break

    if command[0] == 'Rate:':

        new_plant = command[1]
        new_rating = int(command[2])
        garden[new_plant][1].append(new_rating)
    if command[0] == 'Update:':

        name = command[1]
        new_rarity = int(command[2])
        garden[name] = new_rarity,garden[name][1]

    if command[0] == 'Reset:':
        plant = command[1]
        garden[plant] = garden[plant][0],0

print(f"Plants for the exhibition:")

for item in garden:
    print(f"- {item}; Rarity: {garden[item][0]}; Rating: {sum(garden[item][1])}")