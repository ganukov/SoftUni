def imitation_game():
    text = input()
    new_text = list(text)
    while True:
        command = input().split('|')

        if command[0] == 'Decode':
            print(f"The decrypted message is: {''.join(new_text)}")
            break

        if command[0] == 'Move':
            number_of_letters = int(command[1])
            for s,y in enumerate(new_text[0:number_of_letters]):
                new_text.append(y)
                new_text.remove(y)

        if command[0] == 'Insert':
            index = int(command[1])
            value = command[2]
            new_text.insert(index,value)
        if command[0] == 'ChangeAll':
            substring = command[1]
            replacement = command[2]
            new_text[:] = [x if x != command[1] else command[2] for x in new_text]



imitation_game()
