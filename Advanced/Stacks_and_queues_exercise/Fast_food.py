from collections import deque

quantity = int(input())
order = input()

orders = deque(order.split())

biggest = []
for each in orders:
    biggest.append(int(each))

print(max(biggest))

while orders:
    current_order = int(orders.popleft())
    if quantity >= current_order:
        quantity -= current_order
    else:
        orders.appendleft(str(current_order))
        asd = list(orders)
        print(f"Orders left: {' '.join(asd)}")
        break
else:
    print(f"Orders complete")











