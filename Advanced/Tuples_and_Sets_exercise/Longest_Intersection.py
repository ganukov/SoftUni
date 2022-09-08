number = int(input())
best_intersection = set()

for _ in range(number):
    ranges = input().split('-')
    ranges1 = ranges[0]
    ranges2 = ranges[1]
    range1 = ranges1.split(',')
    range1_start = int(range1[0])
    range1_end = int(range1[1])
    range2 = ranges2.split(',')
    range2_start = int(range2[0])
    range2_end = int(range2[1])

    first_set = set(range(range1_start,range1_end + 1))
    second_set= set(range(range2_start,range2_end + 1))
    current_intersection = first_set.intersection(second_set)
    if len(current_intersection) > len(best_intersection):
        best_intersection = current_intersection

print(f'Longest intersection is [{", ".join([str(x) for x in best_intersection])}] with length {len(best_intersection)}')