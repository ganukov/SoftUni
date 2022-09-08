budget = float(input())
count_st = int(input())
price_per_1 = float(input())

decor = budget * 0.10
clothes_money = count_st * price_per_1

if count_st > 150:
    clothes_money -= clothes_money * 0.10

money_movie = clothes_money + decor

diff = abs(budget - money_movie)

if money_movie <= budget:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")

