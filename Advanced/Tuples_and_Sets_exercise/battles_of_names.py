n = int(input())

name_digits_even = set()
name_digits_odd = set()

for row in range(1, n + 1):
    name = input()
    name_sum = sum([ord(o) for o in name]) // row
    if name_sum % 2 == 0:
        name_digits_even.add(name_sum)
    else:
        name_digits_odd.add(name_sum)
sum_odds = sum(name_digits_odd)
sum_evens = sum(name_digits_even)

if sum_evens == sum_odds:
    result = name_digits_odd.union(name_digits_even)
elif sum_evens > sum_odds:
    result = name_digits_odd.symmetric_difference(name_digits_even)
else:
    result = name_digits_odd.difference(name_digits_even)

print(*result, sep=', ')