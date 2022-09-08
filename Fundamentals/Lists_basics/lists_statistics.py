n = int(input())
positive = []
negative = []
sum_of_negatives = 0


for _ in range(n):
    number = int(input())
    if number >= 0:
        positive.append(number)
    else:
        negative.append(number)
        sum_of_negatives += number
print(positive)
print(negative)
print(f"Count of positives: {len(positive)}")
print(f"Sum of negatives: {sum_of_negatives}")
