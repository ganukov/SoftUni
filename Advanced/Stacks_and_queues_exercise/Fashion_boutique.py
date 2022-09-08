clothes = [int(x) for x in input().split()]
capacity_per_rack = int(input())

current_rack_capacity = capacity_per_rack
racks_counter = 1

while clothes:
    piece = clothes[-1]
    if piece > current_rack_capacity:
        racks_counter += 1
        current_rack_capacity = capacity_per_rack
    else:
        current_rack_capacity -= piece
        clothes.pop()

print(racks_counter)