numbers = input().split(" ")
cars = 2
sum_of_times_first = 0
sum_of_times_second = 0

for each_shuffle in range(cars):
    half_deck = int(len(numbers) / 2)
    first_car_times = numbers[:half_deck]
    second_car_times = numbers[-half_deck:]
    second_car_times.reverse()
    numbers = []
    for i in first_car_times:
        sum_of_times_first += int(i)
        if i == "0":
            sum_of_times_first -= sum_of_times_first * 0.2
    for num in second_car_times:
        sum_of_times_second += int(num)
        if num == "0":
            sum_of_times_second -= sum_of_times_second * 0.2
if sum_of_times_first > sum_of_times_second:
    print(f"The winner is right with total time: {sum_of_times_second:.1f}")
else:
    print(f"The winner is left with total time: {sum_of_times_first:.1f}")
