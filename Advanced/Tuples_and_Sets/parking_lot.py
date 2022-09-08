n = int(input())
s = set()

for _ in range(n):
    info = input().split(', ')
    direction = info[0]
    plate = info[1]
    if direction == 'IN':
        s.add(plate)
    elif direction == 'OUT':
        s.remove(plate)

if s:
    for each in s:
        print(each)
else:
    print('Parking Lot is Empty')