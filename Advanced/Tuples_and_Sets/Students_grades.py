number_students = int(input())
d = {}

for each in range(number_students):
    info = input().split()
    name = info[0]
    grade = float(info[1])

    if name not in d:
        d[name] = [grade]
    else:
        d[name].append(grade)

for x,y in d.items():
    y_formatted = ' '.join(f'{yy:.2f}' for yy in y)
    print(f'{x} -> {y_formatted} (avg: {sum(y) / len(y):.2f})')