def even_odd(*args):
    odds = []
    evens = []
    for i in args[0:-1]:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    if args[-1] == 'even':
        return evens
    elif args[-1] == 'odd':
        return odds


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
