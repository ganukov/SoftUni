def print_func(force_user_dict):

    for key, value in force_user_dict.items():
        if len(value) > 0:
            new_line = "\n! "
            print(f"Side: {key}, Members: {len(value)}\n! {new_line.join(value)}")


def force_book():
    force_user_dict = {}

    while True:
        command = input()

        if command == "Lumpawaroo":
            break

        if " | " in command:
            force = command.split(' | ')
            force_side = force[0]
            force_user = force[1]
            if force_side not in force_user_dict:
                force_user_dict[force_side] = [force_user]
            if force_user in force_user_dict.values():
                force_user_dict[force_side].append(force_user)

        elif " -> " in command:
            force = command.split(' -> ')
            force_user = force[0]
            force_side = force[1]
            if force_user in force_user_dict.values():
                force_user_dict[force_user].remove(force_user)
                force_user_dict[force_side].append(force_user)
            if force_user not in force_user_dict.values():
                force_user_dict[force_side].append(force_user)

            elif force_user not in force_user_dict.values() and force_side not in force_user_dict.keys():
                force_user_dict[force_side] = force_user
            print(f"{force_user} joins the {force_side} side!")
    print_func(force_user_dict)





force_book()