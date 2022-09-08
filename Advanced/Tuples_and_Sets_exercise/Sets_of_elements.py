nums = input().split()
n = int(nums[0])
m = int(nums[1])
n_set = set()
m_set = set()
total = n + m


for each in range(n):
    num = int(input())
    n_set.add(num)
for i in range(m):
    numm = int(input())
    m_set.add(numm)

asd = n_set.intersection(m_set)
print('\n'.join([str(x) for x in asd]))