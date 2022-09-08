kind_p = input()
r = int(input())
c = int(input())
price = 0

if kind_p == "Premiere":
    price = 12.00
elif kind_p == "Normal":
    price = 7.50
elif kind_p == "Discount":
    price = 5.00
money_earned = r * c * price
print(f"{money_earned:.2f} leva.")


