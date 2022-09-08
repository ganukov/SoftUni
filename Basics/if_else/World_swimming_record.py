import math
record_time = float(input())
distance = float(input())
time_per_1_meter = float(input())

time = distance * time_per_1_meter
velocity = int(distance / 15) * 12.5

time_Ivan = time + velocity

if time_Ivan < record_time:
    print(f"Yes, he succeeded! The new world record is {time_Ivan:.2f} seconds.")
else:
    diff = abs(record_time - time_Ivan)
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
