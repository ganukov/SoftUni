par_1 = input()
par_2 = int(input())
par_3 = int(input())


def solve(par_1,par_2,par_3):
    result = None

    if par_1 == "multiply":
        result = par_2 * par_3
    elif par_1 == "divide":
        result = par_2 / par_3
    elif par_1 == "add":
        result = par_2 + par_3
    elif par_1 == "subtract":
        result = par_2 - par_3
    return int(result)


print(solve(par_1,par_2,par_3))