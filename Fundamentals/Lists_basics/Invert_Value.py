numbers = input().split(" ")
new_list = []

for each_number in numbers:
    if int(each_number) >= 0:
        new_list.append(-int(each_number))
    else:
        new_list.append(abs(int(each_number)))

print(new_list)