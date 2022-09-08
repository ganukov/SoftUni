number = int(input())
valid = number > 10 and number % 2 == 0
if not valid:
    print("Invalid")
