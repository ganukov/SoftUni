town = input()
sales_volume = float(input())
comission = -1
if town == "Sofia":
    if 0 <= sales_volume <= 500:
        comission = 0.05
    elif 500 < sales_volume <= 1000:
        comission = 0.07
    elif 1000 < sales_volume <= 10000:
        comission = 0.08
    elif sales_volume > 10000:
        comission = 0.12
elif town == "Varna":
    if 0 <= sales_volume <= 500:
        comission = 0.045
    elif 500 < sales_volume <= 1000:
        comission = 0.075
    elif 1000 < sales_volume <= 10000:
        comission = 0.10
    elif sales_volume > 10000:
        comission = 0.13
elif town == "Plovdiv":
    if 0 <= sales_volume <= 500:
        comission = 0.055
    elif 500 < sales_volume <= 1000:
        comission = 0.08
    elif 1000 < sales_volume <= 10000:
        comission = 0.12
    elif sales_volume > 10000:
        comission = 0.145

if comission >= 0:
    print(f"{sales_volume * comission:.2f}")
else:
    print("error")

