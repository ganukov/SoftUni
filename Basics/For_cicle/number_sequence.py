import sys

n = int(input())
#Momentniq maximum
max = -sys.maxsize
#Momentniq minimum
min = sys.maxsize
for number in range(1, n + 1):
    value = int(input())
    #Proverka dali e max
    if value > max:
        max = value
    #Proverka dali e min
    if value < min:
        min = value

print(f"Max number: {max}")
print(f"Min number: {min}")