nums = int(input())
vip = set()
regular = set()

for x in range(nums):
    reservation_codes = input()

    if len(reservation_codes) == 8 and reservation_codes[0].isdigit():
        vip.add(reservation_codes)
    elif len(reservation_codes) == 8:
        regular.add(reservation_codes)

while True:
    guests = input()

    if guests == 'END':
        print(len(vip.union(regular)))
        [print(guests) for guests in sorted(vip)]
        [print(guests) for guests in sorted(regular)]
        break

    if guests in vip:
        vip.remove(guests)
    elif guests in regular:
        regular.remove(guests)

