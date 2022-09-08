import math

number_ppl = int(input())
capacity = int(input())

courses = math.ceil(number_ppl/capacity)

print(courses)
