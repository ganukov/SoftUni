holiday_money = float(input())
money_pocket = float(input())
days_counter = 0
spending_counter = 0

while money_pocket < holiday_money and spending_counter < 5:
    command = input()
    money = float(input())
    days_counter += 1
    if command == "save":
        money_pocket += money
        spending_counter = 0
    elif command == "spend":
        money_pocket -= money
        spending_counter += 1
        if money_pocket < 0:
            money_pocket = 0
if spending_counter == 5:
    print("You can't save the money.")
    print(days_counter)
if money_pocket >= holiday_money:
    print(f"You saved the money for {days_counter} days.")