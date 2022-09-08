def factorial(num):
    return 1 if num == 0 or num == 1 else num * factorial(num - 1)


num1 = int(input())
num2 = int(input())
result = factorial(num1) / factorial(num2)
print(f"{result:.2f}")

# f = 1
# if num >=1:
# for i in range(1, num + 1):
# f = f * i
# return f
