numbers = list(map(int, input().split(', ')))
border = 10
nums = []

while len(numbers) > 0:
    nums = ([num for num in numbers if (border - 10) < num <= border])
    print(f"Group of {border}'s: {nums}")
    numbers = [num for num in numbers if (border - 10 < num > border)]
    border += 10
