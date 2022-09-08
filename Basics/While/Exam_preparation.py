bad_grades = int(input())
failed_times = 0
solved_problems_count = 0
grade_sum = 0
last_problem = ""
has_failed = True
while failed_times < bad_grades:
    problem_name = input()
    if problem_name == "Enough":
        has_failed = False
        break
    grade = int(input())
    if grade <= 4:
        failed_times += 1
    grade_sum += grade
    solved_problems_count += 1
    last_problem = problem_name


if has_failed:
    print(f"You need a break, {bad_grades} poor grades.")
else:
    print(f"Average score: {grade_sum / solved_problems_count:.2f}")
    print(f"Number of problems: {solved_problems_count}")
    print(f"Last problem: {last_problem}")
