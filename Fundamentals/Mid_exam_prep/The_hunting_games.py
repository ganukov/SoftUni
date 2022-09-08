days = int(input())
players_count = int(input())
group_energy = float(input())
water_per_person_a_day = float(input())
food_per_person_a_day = float(input())
water_total = float(days * (water_per_person_a_day * players_count))
food_total = float(days * (food_per_person_a_day * players_count))
water_day = 0
food_day = 0

for each_day in range(days):
    energy_lost = float(input())
    group_energy -= energy_lost
    if group_energy < 0:
        break
    water_day += 1

    if water_day >= 2:
        group_energy += 0.05 * group_energy
        water_total -= 0.3 * water_total
        water_day = 0
    food_day += 1
    if food_day >= 3:
        food_total -= food_total / players_count
        group_energy += 0.1 * group_energy
        food_day = 0

if group_energy <= 0:
    print(f"You will run out of energy. You will be left with {food_total:.2f} food and {water_total:.2f} water.")
else:
    print(f"You are ready for the quest. You will be left with - {group_energy:.2f} energy!")