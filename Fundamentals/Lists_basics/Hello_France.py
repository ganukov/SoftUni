items = input().split("|")
budget = int(input())

profit = 0
new_items = []
data_prices = []
condition = False

for current_item in items:
    item_info = current_item.split("->")
    type_of_item = item_info[0]
    price_of_item = float(item_info[1])
    condition = False

    if type_of_item == "Clothes":
        if price_of_item <= 50.00:
            condition = True
    elif type_of_item == "Shoes":
        if price_of_item <= 35.00:
            condition = True
    elif type_of_item == "Accessories":
        if price_of_item <= 20.50:
            condition = True
    if condition:

        if budget >= price_of_item:
            budget -= price_of_item
            profit += 0.40 * price_of_item
            new_price = price_of_item + (price_of_item * 0.40)
            new_items.append(new_price)
            data_prices.append(f"{new_price:.2f}")
print(" ".join(data_prices))
print(f"Profit: {profit:.2f}")

total_sum = budget + sum(new_items)
if total_sum >= 150:
    print(f"Hello, France!")
else:
    print("Not enough money.")