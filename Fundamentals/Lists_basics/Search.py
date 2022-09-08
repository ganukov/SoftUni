n = int(input())
word = input()
my_list = list()
filtered = list()
for i in range(n):
    words = input()
    my_list.append(words)

    if word in words:
        filtered.append(words)

print(my_list)
print(filtered)


