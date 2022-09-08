energy = int(input())
command = input()
won = 0

while energy > 0:
    energy -= int(command)
    won += 1

    if won % 3 == 0:
        energy += won

    if energy < int(command) or energy == 0:
        print(f'Not enough energy! Game ends with {won} won battles and {energy} energy')
        break

    command = input()

    if command == "End of battle":
        print(f'Won battles: {won}. Energy left: {energy} ')
        break

