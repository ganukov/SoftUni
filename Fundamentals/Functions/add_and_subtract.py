one = int(input())
two = int(input())
three = int(input())


def sum_numbers(one, two):
    result = one + two
    return result


def subtract(result, three):
    result_2 = result - three
    return result_2


print(subtract(sum_numbers(one,two),three))
