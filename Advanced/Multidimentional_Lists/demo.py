# list of n '0'

ll = []
n = 5

for _ in range(n):
    ll.append(0)

# matrix of NxM '0'

n = 5
m = 7

mm = []
for _ in range(n):
    ll = []

    for _ in range(m):
        ll.append(0)
    mm.append(ll)

print(mm)

#####Comprehension#####

mm = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12],
]

print(mm)
print(
    [[v + 1 for v in row] for row in mm]
)

####Multidemensional Comprehension####
##RETURNS ONLY 1 LIST##
print(
    [
        v + 1
        for row in mm
        for v in row
    ]
)

# Correct
def remove_odd(ll):
    return [x for x in ll if x % 2 == 0]

print(
    [remove_odd(row) for row in mm]
)

### Diagonals ###

# main
# row_index == column_index
# secondary
# row_index == n - column_index - 1
# below main - column_index < row_index
# above main column_index > row_index
# below or on main column_index <= row_index