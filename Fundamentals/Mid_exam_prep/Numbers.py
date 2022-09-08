info = list(map(int, input().split()))
new = []
average = int(sum(info)) / int(len(info))

for x in info:
    if x > average:
        new.append(x)
while len(new) > 5 :
    new.remove(min(new))
if not new:
    print(f"No")
else:
    sort = sorted(new, key=lambda x: -x)
    print(' '.join(str(s) for s in sort))