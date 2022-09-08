text = input()

while True:
    command = input().split()

    if command[0] == 'Done':
        print(f'Your password is: {text}')
        break

    if command[0] == 'TakeOdd':
        new = ''
        for i in range(1,len(text),2):
            new += text[i]
        text = new
        print(text)
    elif command[0] == 'Cut':
        index = int(command[1])
        length = int(command[2])
        text = text[0:index] + text[index + length ::]
        print(text)
    elif command[0] == 'Substitute':
        substring = command[1]
        substitute = command[2]
        if substring in text:
            new = text.replace(substring,substitute)
            text = new
            print(text)
        else:
            print(f'Nothing to replace!')