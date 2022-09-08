list1 = input().split(", ")
list2 = input()

result = [el for el in list1 if el in list2]
print(result)