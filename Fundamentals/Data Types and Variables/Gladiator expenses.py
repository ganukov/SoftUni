lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0
helmets = 0
swords = 0
shields = 0
armors = 0

for each_fight in range(1, lost_fights + 1 ):
    if each_fight % 2 == 0:
        helmets += 1
    if each_fight % 3 == 0:
        swords += 1
    if each_fight % 2 == 0 and each_fight % 3 == 0:
        shields += 1
        if shields % 2 == 0 :
            armors += 1

expenses = (helmets * helmet_price) + (swords * sword_price) + (shields * shield_price) + (armors * armor_price)
print(f"Gladiator expenses: {expenses:.2f} aureus")
