def find_positive_and_negative(*args):
    positive_sum = 0
    negative_sum = 0
    for i in args:
        if i > 0:
            positive_sum += i
        else:
            negative_sum += i
    return positive_sum, negative_sum


numbers = [int(x) for x in input().split()]
positive_sum, negative_sum = find_positive_and_negative(*numbers)
print(negative_sum)
print(positive_sum)
if abs(negative_sum) > abs(positive_sum):
    print(f"The negatives are stronger than the positives")
else:
    print(f"The positives are stronger than the negatives")
