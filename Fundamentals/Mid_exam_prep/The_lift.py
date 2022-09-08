people = int(input())
lifts = list(map(int, input().split()))

for each in range(len(lifts)):
    while lifts[each] != 4:
        lifts[each] += 1
        people -= 1
        if people <= 0:
            break
if people == 0 and sum(lifts) % 4 != 0:
    print(f"The lift has empty spots!")
    print(' '.join(str(x) for x in lifts))

elif people > 0 and sum(lifts) % 4 == 0:
    print(f"There isn't enough space! {people} people in a queue!")
    print(' '.join(str(x) for x in lifts))
else:
    print(' '.join(str(x) for x in lifts))
