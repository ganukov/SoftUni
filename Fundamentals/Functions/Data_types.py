def result(data_type):
    pass
    if data_type == "int":
        n = int(input())
        print(f"{n * 2}")
    elif data_type == "real":
        n = float(input())
        print(f"{n * 1.5:.2f}")
    else:
        n = input()
        print(f"${n}$")


data_type = input()
result(data_type)