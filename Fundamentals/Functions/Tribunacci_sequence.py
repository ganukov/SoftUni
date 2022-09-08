def seq(n):
    for s in range(1,n):
        if s == 1:
            print(s)
        if s == 2:
            print(s * 2)
        if s == (s - 1)+ (s - 2) + (s - 3):
            print((s - 1) + (s - 2) + (s - 3))


a = 0
b = 0
c = 0
new_list = []
n = int(input())
seq(n)

