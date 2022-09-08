number = int(input())

for each_number in range(1,100):
    if number % 2 != 1 and number % number != 1:
        print("False")
        break
    else:
        print("True")
        break
