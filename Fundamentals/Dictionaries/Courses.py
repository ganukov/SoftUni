def print_func(courses_dict):
    for key,value in courses_dict.items():
        print(f"{key}: {len(value)}")
        new_line = f"\n-- "
        print(f"-- {new_line.join(str(x) for x in value)}")


def courses():
    courses_dict = {}

    while True:
        command = input().split(' : ')

        if command[0] == 'end':
            print_func(courses_dict)
            break

        course_name = command[0]
        student_name = command[1]

        if course_name not in courses_dict:
            courses_dict[course_name] = [student_name]
        else:
            courses_dict[course_name].append(student_name)


courses()