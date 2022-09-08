expected_sum = int(input())
money_needed_condition = False
card_payment_counter = 0
cash_payment_counter = 0
money_needed = 0
cash_payment_condition = False
card_payment_condition = False
sold = 0
while money_needed < expected_sum:
    item_price = input()
    sold += 1
    if item_price == "End":
        money_needed_condition = True
        print(f"Failed to collect required money for charity.")
        break

    money_needed += int(item_price)
    if sold % 2 == 1:
        if int(item_price) >= 100:
            card_payment_condition = True
            print(f"Error in transaction!")
            break
        else:
            card_payment_counter += 1
            print(f"Product sold!")
    elif sold % 2 == 0:
        if int(item_price) <= 10:
            cash_payment_condition = True
            print(f"Error in transaction!")
            break
        else:
            cash_payment_counter += 1
            print(f"Product sold!")
if money_needed >= expected_sum:
    print(f"Average CS: {cash_payment_counter}")
    print(f"Average CC: {card_payment_counter}")
