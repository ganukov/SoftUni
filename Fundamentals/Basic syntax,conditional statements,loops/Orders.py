number_of_orders = int(input())
total_price = 0

for each_order in range(1, number_of_orders + 1,+1):

    price_per_capsule = float(input())
    days = int(input())
    capsules_count = int(input())
    order_price = price_per_capsule * capsules_count * days
    print(f"The price for the coffee is: ${order_price:.2f}")
    total_price += order_price
print(f"Total: ${total_price:.2f}")