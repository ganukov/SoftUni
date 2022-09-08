def office_management(number_of_rooms):
    free_chairs_left = 0
    condition = True

    for each_room in range(1, number_of_rooms + 1):
        data = input().split()
        available_chairs = data[0]
        visitors = int(data[1])
        diff = abs(len(available_chairs) - visitors)
        if len(available_chairs) < visitors:
            condition = False
            print(f"{diff} more chairs needed in room {each_room}")

        elif len(available_chairs) > visitors:
            free_chairs_left += diff
    if condition:
        print(f"Game On, {free_chairs_left} free chairs left")


info = int(input())
office_management(info)