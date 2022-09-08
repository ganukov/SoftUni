letters = int(input())
result = 0
for each_letter in range(letters):
    l = input()

    result += ord(l)
print(f"The sum equals: {result}")
