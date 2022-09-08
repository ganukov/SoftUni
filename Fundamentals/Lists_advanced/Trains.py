wagons = int(input())
train = [0] * wagons

command = input()
while command != "End":
    current = command.split()
    if current[0] == "add":
        train[-1] += int(current[1])
    elif current[0] == "insert":
        train[int(current[1])] += int(current[2])

    elif current[0] == "leave":
        train[int(current[1])] -= int(current[2])
    command = input()
print(train)