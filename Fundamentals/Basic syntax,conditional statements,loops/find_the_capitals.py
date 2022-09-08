word = input()
ind = []

for l in range(len(word)):
    if word[l].isupper():
        ind.append(l)
    else:
        continue
print(ind)

