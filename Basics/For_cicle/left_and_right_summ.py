n = int(input())
left_sum = 0
right_sum = 0

for first_number in range(1, n + 1):
    value = int(input())
    left_sum += value

for second_number in range(1, n + 1):
    value = int(input())
    right_sum += value

#znaem lqvata i dqsnata suma
if left_sum == right_sum:
    print(f"Yes, sum = {right_sum}")
else:
    print(f"No, diff = {abs(left_sum - right_sum)}")
