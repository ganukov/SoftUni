initial_loot = input().split("|")
total = 0
command = input()

while command != "Yohoho!":
    current = command.split()

    if current[0] == "Yohoho":
        pass
        break

    if current[0] == "Loot":
        items = current[1:]
        for item in items:
            if item not in initial_loot:
                initial_loot.insert(0, item)

    elif current[0] == "Drop":
        index = int(current[1])
        if index in range(len(initial_loot)):
            value = initial_loot[index]
            initial_loot.append(value)
            initial_loot.pop(int(index))
    elif current[0] == "Steal":

        count = int(current[1])
        removed = initial_loot[-count:]
        print(", ".join(removed))
        initial_loot = initial_loot[:-count]

    command = input()
if len(initial_loot) > 0:
    for s in initial_loot:
        total += len(s)
    diff = total / (len(initial_loot))
    print(f"Average treasure gain: {diff:.2f} pirate credits.")
else:
    print(f"Failed treasure hunt.")


