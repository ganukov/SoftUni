t = input()

s = []

for each in range(len(t)):
    if t[each] == "(":
        s.append(each)

    elif t[each] == ")":
        start_index = s.pop()
        end_index = each
        print(t[start_index:end_index + 1])
