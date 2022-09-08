nums = int(input())
s = set()

for _ in range(nums):
    name = input()
    s.add(name)
new_lane = '\n'
print(f"{new_lane.join(s)}")