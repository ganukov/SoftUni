days = int(input())
p_a_day = int(input())
expected = float(input())

total = 0

for each_day in range(1, days + 1):
    current = p_a_day
    total += p_a_day
    if each_day % 3 == 0:
        total += 0.5 * current
    if each_day % 5 == 0:
        total -= total * 0.3

if total >= expected:
    print(f"Ahoy! {total:.2f} plunder gained.")
else:
    diff = 100 - (abs(expected - total) * 100) / expected
    print(f"Collected only {diff:.2f}% of the plunder.")
