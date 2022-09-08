start = input()
end = input()
odd_sum = 0

for first_number in range(int(start[0]), int(end[0]) + 1):
    for second_number in range(int(start[1]), int(end[1]) + 1):
        for third_number in range(int(start[2]), int(end[2]) + 1):
            for fourth_number in range(int(start[3]), int(end[3]) + 1):

                if first_number % 2 != 0 and second_number % 2 != 0 and third_number % 2 != 0 and fourth_number % 2 != 0:
                    print(f"{first_number}{second_number}{third_number}{fourth_number}", end=" ")

