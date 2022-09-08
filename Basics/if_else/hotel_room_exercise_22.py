month = input()
count_n = int(input())
price_s = 0.0
price_a = 0.0

if month == "May" or month == "October":
    if count_n > 7:
        price_s = 50 - 0.05 * 50
    if 7 < count_n > 14:
        price_s = 50 - 0.30 * 50
    else:
        price_s = 50
elif month == "June" or month == "September":
    if count_n > 14:
        price_s = 75.20 - 0.20 * 75.20
    else:
        price_s = 75.20
elif month == "July" or month == "August":
    price_s = 76

if month == "May" or month == "October":
    if count_n > 14:
        price_a = 65 - 0.10 * 65
    else:
        price_a = 65
elif month == "June" or month == "September":
    if count_n > 14:
        price_a = 68.70 - 0.10 * 68.70
    else:
        price_a = 68.70
elif month == "July" or month == "August":
    if count_n > 14:
        price_a = 77 - 0.10 * 77
    else:
        price_a = 77
month_price_s = count_n * price_s
month_price_a = count_n * price_a

print(f"Apartment: {month_price_a:.2f} lv.")
print(f"Studio: {month_price_s:.2f} lv.")
