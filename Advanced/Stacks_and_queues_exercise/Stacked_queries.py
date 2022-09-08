s = []
number = int(input())

for each in range(number):
    command = input()
    if '1' in command:
        com = command.split()
        s.append(int(com[1]))

    if command == '2':
        if s:
            s.pop()

    if command == '3':
        if s:
            print(max(s))
    if command == '4':
        if s:
            print(min(s))
reversed_s = []
while s:
    reversed_s.append(str(s.pop()))
print(', '.join(reversed_s))
