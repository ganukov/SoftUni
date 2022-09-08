expression = input()

opening = []
pairs = {
    '(': ')',
    '[': ']',
    '{': '}'
}

balanced = True

for ch in expression:
    if ch in '([{':
        opening.append(ch)
    elif not opening:
        balanced = False
    else:
        last_opening = opening.pop()

        if pairs[last_opening] != ch:
            balanced = False
    if not balanced:
        break

if not balanced or opening:
    print('NO')
else:
    print('YES')