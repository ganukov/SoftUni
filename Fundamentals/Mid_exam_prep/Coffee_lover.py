coffee_stock = input().split(" ")
commands_count = int(input())
for i in range(1,commands_count + 1):
    command = input().split()

    if command[0] == "Include":
        prod = command[1]
        coffee_stock.append(prod)
    elif command[0] == "Remove":
        index = command[1]
        num_coff = int(command[2])
        if 0 < num_coff < len(coffee_stock):
            if index == "first":
                for each in (coffee_stock[0:num_coff]):
                    coffee_stock.remove(each)
            elif index == "last":
                for s in (coffee_stock[-num_coff:]):
                    coffee_stock.remove(s)
    elif command[0] == "Prefer":
        cof_index1 = int(command[1])
        cof_index2 = int(command[2])
        if 0 <= cof_index1 < len(coffee_stock) and 0 <= cof_index1 < len(coffee_stock):
            coffee_stock[cof_index1],coffee_stock[cof_index2] = coffee_stock[cof_index2],coffee_stock[cof_index1]
    elif command[0] == "Reverse":
        coffee_stock.reverse()
print(f"Coffees:")
print(" ".join(coffee_stock))
