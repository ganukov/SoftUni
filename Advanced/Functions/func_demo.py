# def f(*args):
#     print(args)
#
#
# f(1)
# f([1, 2, 3])
# f({'x': 1, 'y': 2})
# f({1, 2, 3})
#
# f(1,2)

def f(**kwargs):  # key-value args
    if 'age' not in kwargs:
        kwargs['age'] = None
    print(kwargs)


print(f(name='Doncho', age=19))
print(f(x=1, y=-11))
print(f(values=[1, 2, 3, 4], pair=(7, 6)))
