words = input().split()
dict = {}
occ = 0
for word in words:
    for each in word:
        if each not in dict:
            dict[each] = 1
        else:
            dict[each] += 1


for key, value in dict.items():
    print(f"{key} -> {value}")