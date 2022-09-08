message = input()

while True:
    command = input().split(':|:')
    if command[0] == 'Reveal':
        print(f"You have a new text message: {message}")

    elif command[0] == 'InsertSpace':
        index = int(command[1])
        space = ' '
        message = message[0:index] + space + message[index::]
        print(f"{message}")
    elif command[0] == 'Reverse':
        substring = command[1]
        if substring in message:
            message = message.replace(substring,'',1) + substring[::-1]
            print(f"{message}")
        else:
            print('error')
    elif command[0] == 'ChangeAll':
        sub = command[1]
        replacement = command[2]
        new_message = message.replace(sub,replacement)
        message = new_message
        print(f"{message}")
