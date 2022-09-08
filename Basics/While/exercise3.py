import math
import sys
max_goals = -sys.maxsize
found_best_player = False
hat_trick = 0
best = ""
command = input()
name = ""
while True:
    goals = int(input())
    name = input()

    if command == "END":
        found_best_player = True
        best = name
        max_goals = goals
        break
    else:
        command = name
    if goals > max_goals:
        max_goals = goals
        best = name
    if max_goals > 3:
        hat_trick += 1

    if max_goals >= 10:
        best = name
        max_goals = goals
        break

if not found_best_player:
    print(f"{best} is the best player")

if hat_trick > 1:
    print(f"He has scored {max_goals} and made a hat trick!")
else:
    print(f"{name} scored {max_goals}")
