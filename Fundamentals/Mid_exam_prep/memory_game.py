def matching(data,index1,index2):
    data.pop(int(index1))
    data.pop(int(index2))
    return f"Congrats! You have found matching elements - {index1}!"


def cheating(data,index1,index2):
    half_seq = int(len(data)) / 2
    data.insert(half_seq,int(f" -{moves_counts}a"))
    data.insert(half_seq + 1, int(f" -{moves_counts}a"))
    return f"Invalid input! Adding additional elements to the board"


def memory_game(data):
    moves_counts = 0

    while True:
        command = input().split()

        if command == "end":
            print(" ".join(data))
            break

        moves_counts += 1

        index1 = command[0]
        index2 = command[1]

        if index1 == index2 or int(index1) < 0 or int(index2) < 0:
            data = cheating(data,index1,index2)

        if data[int(index1)] == data[int(index2)]:
            data = matching(data, index1, index2)

        elif data[int(index1)] != data[int(index2)]:
            print(f"Try again!")

    if len(data) == 0:
        print(f"You have won in {moves_counts} turns!")
    if len(data) != 0:
        print(f"Sorry you lose :(")
        print(data)
    command = input().split()

moves_counts = 0
seq = input().split()
memory_game(seq)