budget = float(input())
seasons = input()
money_spent = 0
destination = ""
place = ""
if budget <= 100:
    destination = "Bulgaria"
    if seasons =="summer":
        place = "Camp"
        money_spent = 0.30 * budget
    elif seasons == "winter":
        place = "Hotel"
        money_spent = 0.70 * budget
elif 100 < budget <= 1000:
    destination = "Balkans"
    if seasons == "summer":
        place = "Camp"
        money_spent = 0.40 * budget
    elif seasons == "winter":
        place = "Hotel"
        money_spent = 0.80 * budget
elif budget > 1000:
    destination = "Europe"
    place = "Hotel"
    if seasons == "summer" or seasons == "winter":
        money_spent = 0.90 * budget

print(f"Somewhere in {destination}")
print(f"{place} - {money_spent:.2f}")
