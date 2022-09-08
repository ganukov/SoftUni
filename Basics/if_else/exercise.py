age = float(input())
sex = input()

if sex == "f":
    if age <= 16:
        print("Miss.")
    else:
        print("Mrs.")
else:
    if age <= 16:
        print("Mr.")
    else:
        print("Master.")
