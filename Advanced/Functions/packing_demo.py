# ll1 = [1, 2, 3, 4]
#
# k, l, *r = ll1
# print(k, l, r)
#
# ll2 = [-1, *ll1, -2]
# print(ll2)
#
# dd1 = {
#     'x': 1,
#     'y': 2
# }
#
# dd2 = {
#     'z': 3,
#     **dd1,
# }
# print(dd2)
def f(*args, **kwargs):
    print(f'args = {args}, kwargs = {kwargs}')


numbers = [1, 2, 3, 4, 5]
grade_dict = {
    'Donch': 3,
    'Ivan': 4,
    'Maria': 6,
    'Pesho': 4.5
}

f(*numbers)
f(**grade_dict)
f(*numbers,**grade_dict)