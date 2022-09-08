size_1 = int(input())
size_2 = int(input())
size_3 = int(input())
size = size_1 * size_2 * size_3
full_room = False
place_taken = 0

while place_taken <= size:
    boxes_count = input()

    if boxes_count == "Done":
        if place_taken < size:
            full_room = True
        elif place_taken >= size:
            full_room = True
        break
    elif place_taken >= size:
        full_room = True
        break
    place_taken += int(boxes_count)

diff = abs(size - place_taken)
if full_room:
    print(f"{diff} Cubic meters left.")
else:
    print(f"No more free space! You need {diff} Cubic meters more.")