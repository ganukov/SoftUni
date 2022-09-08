rows = int(input())
my_dict = {}

for each in range(rows):
    name = input()
    grade = float(input())

    if name not in my_dict:
        my_dict[name] = [grade]
    else:
        my_dict[name].append(grade)

for key, value in my_dict.items():
    average = sum(value) / len(value)
    if average >= 4.50:
        print(f"{key} -> {average:.2f}")