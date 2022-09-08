def parking():
    number = int(input())
    register_dict = {}

    for each in range(number):
        command = input().split()
        if command[0] == 'register':

            name = command[1]
            plate = command[2]

            if name in register_dict:
                print(f"ERROR: already registered with plate number {plate}")
            else:
                register_dict[name] = plate
                print(f"{name} registered {plate} successfully")

        elif command[0] == "unregister":
            name = command[1]

            if name not in register_dict:
                print(f"ERROR: user {name} not found")
            else:
                register_dict.pop(name)
                print(f"{name} unregistered successfully")

    for key,value in register_dict.items():
        print(f"{key} => {value}")


parking()
