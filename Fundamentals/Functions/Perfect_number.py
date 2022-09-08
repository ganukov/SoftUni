def perfect_number(number):
    pass
    for each in range(1, number):
        if number % each == 0:
            num_list.append(each)
    result = sum(num_list)
    if result == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


number = int(input())
num_list = []
perfect_number(number)






