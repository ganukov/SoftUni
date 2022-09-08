numbers = input().split()
copy_list = list(map(float,numbers))
new_list = []
for each in copy_list:
    new_list.append(abs(each))

print(new_list)