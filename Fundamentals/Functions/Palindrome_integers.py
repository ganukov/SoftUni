def palindrome_func(nums):
    pass
    for num in nums:
        if num == num[::-1]: # обръщаме числото отзад напред !!!
            print("True")
        else:
            print("False")


numbers = input().split(", ")
palindrome_func(numbers)