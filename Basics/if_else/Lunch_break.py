from math import ceil
serials_name = input()
time_per_episod = int(input())
time_for_break = int(input())

time_for_lunch = time_for_break / 8
time_for_free = time_for_break / 4
time_left = time_for_break - (time_for_lunch + time_for_free)

diff = abs(time_left - time_per_episod)

if time_left >= time_per_episod:
    print(f"You have enough time to watch {serials_name} and left with {ceil(diff)} minutes free time.")
else:
    print(f"You don't have enough time to watch {serials_name}, you need {ceil(diff)} more minutes.")
