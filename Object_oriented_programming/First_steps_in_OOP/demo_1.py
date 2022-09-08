###################### 1 ####################
# enables extensibility
def print_list(ll):
    [print(x) for x in ll if x is not None]
    # когато ползваме функции си правим по лесно да променим кода
    # в бъдеще ако ни се наложи!!!


ll = [1, 2, 3, 4, 5, 6]
print('Printing first list')
print_list(ll)

ll2 = [6, 5, 4, 3, 2, 1]
print('Printing second list')
print_list(ll2)

########## B #######
# a single Function should complete a single task // should be COHERENT
# кода трябва да е разбираем и целенасочен

