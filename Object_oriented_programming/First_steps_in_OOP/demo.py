# 1 Project Architecture
# 2 Scope and Namespace
# 3 Basics of OOP
    # Object
    # Class
    # Instance
# 4 Creating and Using Classes
############2############
#Scope and Namespace
#a Local
#b Global
#c Built-In Namespaces
#What is Namespace?
# A mapping from names to objects
#examples: Built-in names,for example abs()function
# Global names in module
# Local names in module

# 1 >>> Splitting Code into Functions
    # We use methods to split code into functional blocks
    # Improves code readability
    # Allows for easier debugging

############2############
#Scope and Namespace
#a Local
#b Global
#c Built-In Namespaces
#What is Namespace?
# A mapping from names to objects
#examples:  # Built-in names,for example abs()function ползваме без да дефинираме
            # Global names in module са който дефинираме или импортваме
            # Local names in module са само в дефинираното тяло
    #### EXAMPLES ####
#print() and sum() = built-in namespace
#Global namespace (global for this module) module is every file in python
def sum1(ll):
    #result and x - in local namespace(local for func body and class)
    result = 1
    for x in ll:
        result += x
    return result


print(sum1([1,2,3,4]))
#### WHAT IS A SCOPE? ####
# namespace = мястото където живеят променливите
# scope = мястото където използваме тези променливи вкл. функции
# scopes = 3 of a kind
# - Global scope ( module )
# - Function scope ( func )
# - Class scope ( from function scope )
#example#

text = 'Hello from global'
def print_greeting():
    text = 'Hello from func scope' ## Class scope ## not changing the global "text"
    print(text)
print_greeting()
print(text)
# how to get the different scope variables # - global / nonlocal
###examples###
#####################GLOBAL########################

print_count = 0


def print_list(ll):
    global print_count # global makes var like an object of a reference type
    print_count += 1
    print(ll)
ll = list(range(5))
print(print_count)
print_list(ll)
print(print_count)
print_list(ll)
print(print_count)
print_list(ll)
print(print_count)
print_list(ll)
print(print_count)
print_list(ll)
##########################NONLOCAL#########################
def f1():
    count = 0
    def f1_ineer():
        nonlocal count # get from parent scope
        count += 1
    for _ in range(5):
        f1_ineer()
        print(count)
f1()

############ 3 ################## OOP #######

        ## what is oop ##
# its the most popular programing paradigm
# it relies on classes and objects
# a CLASS is used to create individual instance of object !

        ### advantages of OOP###
# clear structure and clean code
# easy to write
# can test each behavior of an object separately
# easy maintenance and modification !!!
        ### Objects in Python###
# Everything in Python is an object and has a type !!!
    # 10.5
    # Python
    # [1,2,3,4]
        ### what is an object ###
# object пази стойност и има интерфейс
# internal represеntation позволява на object да работи
# state = това което прави един обект уникален
# behavior = the tasks that an object performs
        ### WHAT IS A CLASS ###
# a Class is a type we create or is built-in(list,set,int,str)
# func in Class is called METHOD
