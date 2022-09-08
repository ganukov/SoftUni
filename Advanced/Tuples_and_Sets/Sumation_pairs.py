nums = [int(x) for x in input().split()]
target_num = int(input())
iterations = 0
s = set([])
d = {}
for each in nums:
    if each in s:
        p1 = each
        p2 = d[each]
        print(f'{p2} + {p1} = {target_num}')

    else:
        s.add(target_num - each)
        d[target_num - each] = each
