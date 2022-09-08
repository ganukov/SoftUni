def shooting(data):
    count = 0
    while True:
        new = []
        command = input()

        if command == "End":
            print(f"Shot targets: {count} -> {' '.join(map(str, targets))}")
            break

        index = int(command[0])
        if index in range(len(data)):
            current = data[index]
            for i in range(len(data)):
                if data[i] != -1:
                    if data[i] > current:
                        data[i] -= current
                    else:
                        data[i] += current
            data[index] = -1
            count += 1


targets = list(map(int,input().split()))
shooting(targets)