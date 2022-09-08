population = list(map(int, input().split(', ')))
min_wealth = int(input())
max_num = max(population)
new = []
if sum(population) % min_wealth == 0:
    for each in population:
        if each < min_wealth:
            each += min_wealth - each
        if max(population) > min_wealth:


        new.append(each)
    if max(new) != max_num:
        new.remove(max(new))
        new.append(max_num)

    print(new)
else:
    print(f"No equal distribution possible")
