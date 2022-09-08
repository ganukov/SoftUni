cards = input().split(" ")
shuffles = int(input())


for each_shuffle in range(shuffles):
    half_deck = int(len(cards) / 2)
    first_half = cards[:half_deck]
    second_half = cards[-half_deck:]
    cards = []
    for p in range(half_deck):
        cards.append(first_half[p])
        cards.append(second_half[p])

print(cards)

