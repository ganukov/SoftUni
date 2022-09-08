budget = float(input())
price_per_1_kg_flour = float(input())
pack_eggs = price_per_1_kg_flour * 0.75
price_for_milk = (price_per_1_kg_flour + price_per_1_kg_flour * 0.25) / 4
price_per_bread = pack_eggs + price_per_1_kg_flour + price_for_milk
count_bread = 0
colored_eggs = 0
money_left = 0

while budget > 0:
    budget -= price_per_bread

    if budget <= 0:
        break
    count_bread += 1
    colored_eggs += 3
    if count_bread % 3 == 0:
        colored_eggs -= (count_bread - 2)
    money_left = budget

print(f"You made {count_bread} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")