nums_str = input()
numbers = [float(x) for x in nums_str.split(' ')]
a = {}

for each in numbers:
    if each not in a:
        a[each] = 0
    a[each] += 1

for x,y in a.items():
    print(f'{x:.1f} - {y} times')
