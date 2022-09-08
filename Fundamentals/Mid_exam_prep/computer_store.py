import sys

taxes = 0
total_price = 0
price_not_taxed = 0
parts_price = input()

while parts_price != "special" and parts_price != "regular":

    total_price = 0
    if float(parts_price) < 0:
        print("Invalid price!")
        parts_price = 0
    price_not_taxed += float(parts_price)
    tax_current = 0.2 * float(parts_price)
    taxes += tax_current
    total_price += price_not_taxed + taxes
    parts_price = input()

if parts_price == "special":
    if total_price == 0:
        print("Invalid order!")
        sys.exit()
    total_price -= total_price * 0.1
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_not_taxed:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print(f"-----------")
    print(f"Total price: {total_price:.2f}$")

elif parts_price == "regular":
    if total_price == 0:
        print("Invalid order!")
        sys.exit()
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_not_taxed:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print(f"-----------")
    print(f"Total price: {total_price:.2f}$")



