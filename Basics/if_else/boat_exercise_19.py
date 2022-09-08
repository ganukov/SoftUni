budget = int(input())
season = input()
count_f = int(input())
discount = 0
price = 0
discount_2 = 0
if season == "Spring":
    price = 3000
elif season == "Summer" or season == "Autumn":
    price = 4200
elif season == "Winter":
    price = 2600
if count_f <= 6:
    discount = 0.10
elif 7 <= count_f <= 11:
    discount = 0.15
elif count_f > 12:
    discount = 0.25

if count_f % 10 == 0 and season != "Autumn":
    discount_2 = 0.05

money_spent = price - discount * price - discount_2 * price
money_left = abs(money_spent - budget)
if money_spent <= budget:
    print(f"Yes! You have {money_left:.2f} leva left.")
elif money_spent > budget:
    print(f"Not enough money! You need {money_left:.2f} leva.")

