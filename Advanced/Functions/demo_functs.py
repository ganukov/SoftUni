ll = [1, 2, 3, 4]
tt = (1, 2, 3, 4)

# x = ll[0]
# y = ll[1]
# z = ll[2]
# a = ll[3]
###Unpacking###

##syntactic sugar##
x, y, z, a = ll
print(x)
print(y)
print(z)
print(a)

k, *_, r = ll
print(k)

print(r)


###RECURSION###

def reverse_loop(n):
    if n < 0: # exit case / base case
        return # same as 'break' in 'while' loop
    print(n)
    reverse_loop(n - 1) # recursive call


def loop(n):
    if n < 0:
        return

    loop(n - 1) # recursive call
    print(n)

print(f'-----Reverse loop----')
reverse_loop(5)

print(f'----Forward loop----')
loop(5)