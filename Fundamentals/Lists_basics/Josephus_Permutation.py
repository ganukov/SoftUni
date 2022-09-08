people = input().split()
k = int(input())
executed = []
counter = 0
index = 0

while len(people) > 0:
    counter += 1
    if counter % k == 0:
        executed.append(people.pop(index))
    else:
        index += 1
    if index >= len(people):
        index = 0

print([",".join(executed)])