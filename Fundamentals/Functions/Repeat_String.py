word = input()
n = int(input())

repeat_string = lambda a, b: a * b
result = repeat_string(word, n)
print(result)
