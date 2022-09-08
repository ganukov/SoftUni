gifts = input().split()
command = input().split()
end = ["No", "Money"]
while command != end:
    if "OutOfStock" in command:
        for i , value in enumerate(gifts):
            if value == str(command[1]):
                gifts[i] = "None"
    elif "Required" in command:
        if 0 < int(command[2]) < len(gifts):
            gifts[int(command[2])] = command[1]
    elif "JustInCase" in command:
        gifts[-1] = command[1]

    command = input().split()
while "None" in gifts:
    gifts.remove("None")
print(" ".join(gifts))