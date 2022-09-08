info = input().split(', ')
rows = int(info[0])
columns = int(info[1])
total = 0
b = []
for _ in range(rows):
    nums = [int(x) for x in input().split(', ')]
    b.append(nums)

for each in b:
    total += sum(each)

print(total)
print(b)