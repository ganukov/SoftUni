numbers = input().split(" ")
copy_nums = list(map(int, numbers))
n = int(input())


for each in range(n):
    min_num = min(copy_nums)
    numbers.remove(str(min_num))
    copy_nums.remove(min_num)

print(", ".join(numbers))