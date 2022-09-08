n = int(input())
chems = set()

for _ in range(n):
    chem_comps = input()
    splitted = chem_comps.split()
    for each in splitted:
        chems.add(each)

print('\n'.join(chems))
