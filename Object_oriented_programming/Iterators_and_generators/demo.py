# ITERATORS AND GENERATORS#


# What are iterators:
# Iterator is an object that can be iterated upon
# it will return data one element at a time
# we use 2 dunder methots :
# __iter__ and __next__
# __iter__ = internal dunder method in class
# iter() = external from class function,that calls __iter__
# how for loop is implemented:


# ll_iter = iter([1,2,3,4])

# while True:
#   try:
#       print(ll_iter)
#   except:
#       raise StopIteration()

#### Syntactic Sugar ####
# Generators
# yield is a keyword
# return = stops the whole function
# yield = pauses it and when its called again carries on to the next one
# with generators we write iterators easily
# yield makes the function a GENERATOR

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __iter__(self):
        # yield ('name', self.name)
        # yield ('age', self.age)
        for pair in self.__dict__.items():
            yield pair


doncho = Person('Doncho', 19)
for x in doncho:
    print(x)

### Generator Expressions or Generator comprehensions
#we make generator function through comprehension


#[ -> literal for list comprehension
#{ -> literal for set or dict comprehension
#( -> literal for generator expression

'''
Generators are syntax sugar for iterators
Generator expressions are syntax sugar for generators
'''


def get_func1(n):
    print('The start')
    for x in range(n):
        yield x


def get_func(n):
    print('The start')
    for x in range(n):
        yield x


print(get_func(5))
gf = get_func(5)
print(next(gf))
print(next(gf))
print(next(gf))
print(next(gf))
print(next(gf))
