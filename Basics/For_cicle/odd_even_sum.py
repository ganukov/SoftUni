n = int(input())
odd_sum = 0
even_sum = 0

for number in range(1, n + 1):
    value = int(input())
    if number % 2 == 0:
        even_sum += value
    else:
        odd_sum += value

if odd_sum == even_sum:
    print(f"Yes")
    print(f"Sum = {even_sum}")
else:
    print(f"No")
    print(f"Diff = {abs(odd_sum - even_sum)}")
