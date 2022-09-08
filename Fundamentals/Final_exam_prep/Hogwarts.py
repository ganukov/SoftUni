spell = input()

while True:
    command = input().split()

    if command[0] == 'Abracadabra':
        break

    elif command[0] == 'Abjuration':
        spell = spell.upper()
        print(spell)
    elif command[0] == 'Necromancy':
        spell = spell.lower()
        print(spell)
    elif command[0] == 'Illusion':
        index = int(command[1])
        letter = command[2]
        if 0 <= index < len(spell):
            spell = spell[0:index] + letter + spell[index + 1:]
            print(f'Done!')
        else:
            print(f'The spell was too weak.')
    elif command[0] == 'Divination':
        first_substring = command[1]
        second_substring = command[2]
        if first_substring in spell:
            new = spell.replace(first_substring,second_substring)
            spell = new
            print(spell)
    elif command[0] == 'Alteration':
        substring = command[1]
        if substring in spell:
            mew = spell.replace(substring,'')
            spell = mew
            print(spell)
    else:
        print(f'The spell did not work!')