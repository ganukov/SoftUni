def orders_func(orders_dic, info_products):
    product = info_products[0]
    price = float(info_products[1])
    quantity = int(info_products[2])

    if product not in orders_dic:
        orders_dic[product] = [price, quantity]
    else:
        orders_dic[product] = [price, (quantity + orders_dic[product][1])]
    return orders_dic


def orders():
    orders_dic = {}

    while True:
        command = input()

        if command == 'buy':
            break

        info_products = command.split()
        orders_dic = orders_func(orders_dic, info_products)

    for i in orders_dic:
        total_sum = orders_dic[i][0] * orders_dic[i][1]
        print(f'{i} -> {total_sum:.2f}')


orders()