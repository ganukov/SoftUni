def decipher(word):
    string = list(word)
    num = list()

    while string[0].isdigit():
        num.append(string[0])
        string.pop(0)

    num = int("".join(num))
    string.insert(0, chr(num))
    return "".join(string)


def switch(word):
    letters = list(word)
    letters[1], letters[-1] = letters[-1], letters[1]
    return ''.join(letters)


print(' '.join([switch(decipher(word)) for word in input().split()]))