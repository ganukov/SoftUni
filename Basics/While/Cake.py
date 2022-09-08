size_1 = int(input())
size_2 = int(input())
size_cake = size_1 * size_2
pieces = 0
pieces_condition = False
while True:
    pieces_taken = input()

    if pieces_taken == "STOP":
        break

    pieces += int(pieces_taken)
    if pieces > size_cake:

        break


diff = abs(size_cake - pieces)
if size_cake > pieces:
    print(f"{diff} pieces are left.")
else:
    print(f"No more cake left! You need {diff} pieces more.")

