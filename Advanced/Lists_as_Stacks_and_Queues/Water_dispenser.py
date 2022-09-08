from collections import deque

d = deque()

water = int(input())

name = input()
while name != "Start":
    d.append(name)
    name = input()
    if name == "Start":
        while True:
            command = input()

            if command == "End":
                print(f"{water} liters left")
                break

            if command.isdigit():
                liters = int(command)
                if liters <= water:
                    print(f"{d.popleft()} got water")
                    water -= liters
                else:
                    print(f"{d.popleft()} must wait")
            else:
                com = command.split()
                liters1 = int(com[1])
                water += liters1
