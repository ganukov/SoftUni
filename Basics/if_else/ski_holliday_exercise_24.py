days = int(input())
kind = input()
grade = input()
days -= 1
price = 0
money_spent = days * price
if kind == "room for one person":
    price = 18.00
    money_spent = days * price
elif kind == "apartment":
    price = 25.00
    if days < 10:
        money_spent = days * price - (days * price * 0.30)
    elif 10 < days < 15:
        money_spent = days * price - (days * price * 0.35)
    elif days > 15:
        money_spent = days * price - (days * price * 0.50)
    else:
        money_spent = days * price
elif kind == "president apartment":
    price = 35.00
    if days < 10:
        money_spent = days * price - (days * price * 0.10)
    elif 10 < days < 15:
        money_spent = days * price - (days * price * 0.15)
    elif days > 15:
        money_spent = days * price - (days * price * 0.20)
    else:
        money_spent = days * price

if grade == "positive":
    money_spent = money_spent + 0.25 * money_spent
else:
    money_spent = money_spent - 0.10 * money_spent

print(f"{money_spent:.2f}")

