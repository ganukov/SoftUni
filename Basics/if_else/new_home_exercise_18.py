kind_f = input()
count_f = int(input())
budget = int(input())
discount = 0
price = 0
if kind_f == "Roses":
    price = 5
    if count_f > 80:
        discount = 0.01
elif kind_f == "Dahlias":
    price = 3.80
    if count_f > 90:
        discount = 0.15
elif kind_f == "Tulips":
    price = 2.80
    if count_f > 80:
        discount = 0.15
elif kind_f == "Narcissus":
    price = 3
    if count_f < 120:
        price = 3 + 3 * 0.15
elif kind_f == "Gladiolus":
    price = 2.50
    if count_f < 80:
        price = 2.50 + 2.50 * 0.20

money_spent = count_f * price - discount * (count_f * price)
money_left = abs(budget - money_spent)
if budget >= money_spent:
    print(f"Hey, you have a great garden with {count_f} {kind_f} and {money_left:.2f} leva left.")
else:
    print(f"Not enough money, you need {money_left:.2f} leva more.")
