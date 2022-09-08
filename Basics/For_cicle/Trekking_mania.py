groups_count = int(input())
total_ppl = 0
g1 = 0
g2 = 0
g3 = 0
g4 = 0
g5 = 0

for _ in range(groups_count):
    count_ppl = int(input())
    total_ppl += count_ppl
    if count_ppl <= 5:
        g1 += count_ppl
    elif 6 <= count_ppl <= 12:
        g2 += count_ppl
    elif 13 <= count_ppl <= 25:
        g3 += count_ppl
    elif 26 <= count_ppl <= 40:
        g4 += count_ppl
    elif count_ppl >= 41:
        g5 += count_ppl

g1 = g1 / total_ppl * 100
g2 = g2 / total_ppl * 100
g3 = g3 / total_ppl * 100
g4 = g4 / total_ppl * 100
g5 = g5 / total_ppl * 100


print(f"{g1:.2f}%")
print(f"{g2:.2f}%")
print(f"{g3:.2f}%")
print(f"{g4:.2f}%")
print(f"{g5:.2f}%")
