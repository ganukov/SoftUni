time = int(input()) * 60
time_1 = int(input())
total_time = time + time_1 + 15
hour = total_time // 60
minutes = total_time % 60

if hour == 24:
    hour_1 = 0
    print(f"{hour_1}:{minutes:02d}")
elif 0 <= minutes < 10:
    minutes_1 = 0
    print(f"{hour}:{minutes_1}{minutes}")
else:
    print(f"{hour}:{minutes}")
