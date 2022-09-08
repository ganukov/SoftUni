def swap(data,index1,index2):
    data[int(index1)], data[int(index2)] = data[int(index2)],data[int(index1)]
    return data


def multiply(data,index1, index2):
    m = data[int(index1)] * data[int(index2)]
    data.pop(int(index1))
    data.insert(int(index1), int(m))
    return data


def decrease(data):
    new = [x - 1 for x in data]
    return new


def array_modifier(data):

    while True:
        command = input().split(' ')

        if command[0] == 'end':
            print(', '.join([str(x) for x in data]))
            break
        elif command[0] == 'decrease':
            data = decrease(data)
        else:
            current_command = command[0]
            index1 = command[1]
            index2 = command[2]

            if current_command == 'swap':
                data = swap(data,index1, index2)
            elif current_command == 'multiply':
                data = multiply(data,index1, index2)


numbers = list(map(int, input().split()))
array_modifier(numbers)