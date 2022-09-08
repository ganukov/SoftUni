budget = float(input())
video_cards_count = int(input())
cpu_count = int(input())
ram_count = int(input())

price_v_c = video_cards_count * 250
price_cpu = (price_v_c * 0.35) * cpu_count
price_ram = (price_v_c * 0.10) * ram_count
total_price = price_v_c + price_cpu + price_ram

if video_cards_count > cpu_count:
    total_price -= total_price * 0.15

if budget >= total_price:
    diff = budget - total_price
    print(f"You have {diff:.2f} leva left!")
else:
    diff = abs(budget - total_price)
    print(f"Not enough money! You need {diff:.2f} leva more!")
