activation_key = input()

while True:
    command = input().split('>>>')
    if command[0] == 'Generate':
        print(f"Your activation key is: {activation_key}")

    elif command[0] == 'Contains':
        substring = command[1]
        if substring in activation_key:
            print(f'{activation_key} contains {substring}')
        else:
            print('Substring not found!')
    elif command[0] == 'Flip':
        start_index = int(command[2])
        end_index = int(command[3])
        if command[1] == 'Upper':
            sub = activation_key[start_index:end_index].upper()
            activation_key = activation_key[0:start_index] + sub + activation_key[end_index:]
            print(activation_key)
        elif command[1] == 'Lower':
            sub2 = activation_key[start_index:end_index].lower()
            activation_key = activation_key[0:start_index] + sub2 + activation_key[end_index:]
            print(activation_key)
    elif command[0] == 'Slice':
        s_index = int(command[1])
        e_index = int(command[2])
        activation_key = activation_key[0:s_index] + activation_key[e_index:]
        print(activation_key)

