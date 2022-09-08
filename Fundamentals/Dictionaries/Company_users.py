def company_users():
    companies_dict = {}

    while True:
        command = input().split(' -> ')

        if command[0] == 'End':
            break

        if command[0] not in companies_dict:
            companies_dict[command[0]] = [command[1]]
        else:
            if command[1] not in companies_dict[command[0]]:
                companies_dict[command[0]].append(command[1])

    for key, value in companies_dict.items():
        new_line = f"\n-- "
        print(f"{key}\n-- {new_line.join(str(x) for x in value)}")




company_users()