sublists = input().split('|')

result = []

for idx in range(len(sublists) -1,-1,-1):
    current_el = sublists[idx].strip().split()
    result.extend(current_el)

print(' '.join(result))