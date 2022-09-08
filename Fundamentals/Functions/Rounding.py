numbers = input().split()
copy_numbers = list(map(float, numbers))
new_list = []
for each in copy_numbers:
    new_list.append(round(each))
print(new_list)