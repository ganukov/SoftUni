number_1 = int(input())
number_2 = int(input())
my_list = list()


for each_number in list(range(1, number_2 + 1)):
    my_list.append(each_number * number_1)

print(my_list)