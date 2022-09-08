def Phonebook():
    new_dict = {}
    info = input()

    while not info.isdigit():
        ex = info.split('-')
        name = ex[0]
        number = ex[1]
        new_dict[name] = number
        info = input()
    if info.isdigit():

        for each in range(int(info)):
            name1 = input()
            if name1 not in new_dict:
                print(f"Contact {name1} does not exist.")
            else:
                print(f"{name1} -> {new_dict[name1]}")


Phonebook()
