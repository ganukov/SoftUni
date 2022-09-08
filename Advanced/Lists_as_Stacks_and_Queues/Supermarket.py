from collections import deque

s = deque()

while True:
    name = input()

    if name == "End":
        print(f"{len(s)} people remaining.")
        break

    elif name == "Paid":
        while s:
            print(s.popleft())

    else:
        s.append(name)