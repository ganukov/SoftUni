def fact(n):
    if n in (0, 1):
        return 1
    if n == 0:
        return 1

    n_1_fact = fact(n - 1)
    return n * n_1_fact


print(fact(10))