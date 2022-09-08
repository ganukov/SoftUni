from collections import deque

magic_levels = [int(x) for x in input().split()]
toys = deque([int(x) for x in input().split()])

crafted = {}
current_toys = {
    'Doll': 150,
    'Wooden train': 250,
    'Teddy bear': 300,
    'Bicycle': 400,
}

condition = False

while magic_levels and toys:
    magic_level = magic_levels.pop()
    toy = toys.popleft()

    total_magic = magic_level * toy
    if magic_level == 0 or toy == 0:
        continue
    if total_magic > 0:
        for x,y in current_toys.items():
            if total_magic == y:

                if x not in crafted:
                    crafted[x] = 1
                    condition = True
                else:
                    crafted[x] += 1
                    condition = True

            if total_magic > 0 and total_magic != y:
                toy += 15
                toys.append(toy)

    if total_magic < 0:
        total_magic = magic_level + toy
        magic_levels.append(total_magic)





print(crafted)