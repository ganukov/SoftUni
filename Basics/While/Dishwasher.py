count_bottles = int(input())
count_dishes = 0
count_pots = 0
detergent = count_bottles * 750
enough_detergent = False
loading = 0
detergent_used = 0

while detergent >= detergent_used:
    current_dishes = input()
    loading += 1
    if current_dishes == "End":
        enough_detergent = True
        break

    count_dishes += int(current_dishes)

    if loading % 3 == 0:
        count_pots += int(current_dishes)
        count_dishes -= int(current_dishes)

    detergent_used = count_dishes * 5 + count_pots * 15

diff = abs(detergent - detergent_used)

if enough_detergent:
    print(f"Detergent was enough!")
    print(f"{count_dishes} dishes and {count_pots} pots were washed.")
    print(f"Leftover detergent {diff} ml.")
else:
    print(f"Not enough detergent, {diff} ml. more necessary!")
