####Inheritance####

# 1. Inheritance
# a super() method

# 2. Forms of Inheritance
# a Single Inheritance
# when a child class inherits properties from a SINGLE PARENT class ONLY

# b Multiple Inheritance
# when a child class inherits from MORE THAN ONE PARENT CLASS
# allows modeling of complex relationships
        ##example##
###Father>>>>Child<<<<Mother###


# c Multilevel Inheritance
# when a CHILD CLASS becomes a PARENT CLASS for another CHILD CLASS
# in Python, multilevel inheritance can be done at any depth
        ##Example##
#### Grandpa >>>> Father >>>> Child ####

# d Hierarchical Inheritance
# When more than one CHILD CLASSES are created from A SINGLE PARENT CLASS

# Method resolution order in Python 3 // MRO in Python 3
###This is the order in which methods should be inherited in the presence of
### multiple inheritance
# Python 3 uses the C3 linearization algorithm for MRO
# Its possible to see MRO of a class using mro() method of the class

# 3.Mixins
# Mixin is a class the implements a specific set of features that is needed
# in many different classes
# Mixin is a class with NO DATA, only methods
# Mixins cannot be instantiated by themselves
# We use mixins to extend functionality

            ### MIXINS ADVANTAGES ###

## Provides non-comples mechanisms of multiple inheritance
## Provides code reusability
## Allow inheritance and use of ONLY DESIRED FEATURES FROM THE PARENT CLASS,NOT ALL



#### 1 ####
# Inheritance = Capability of one class to inherit the methods and properties from
# another class
#### benefits ####
# a Code reusability
# b Add features to a class without modifying it
# c It is transitive in nature

##### The super() Method #####
# Its a built-in method with returns a temporary object of the superclass
# ALLOWS YOU TO CALL METHODS OF THE SUPERCLASS IN YOUR SUBCLASS
# EXTENDS THE FUNCTIONALITY OF THE INHERITED METHOD

# Inheritance - extent functionality of existing classes to
# eliminate repetitive code

# Encapsulation - stops objects from interacting with each other so classes cant change
# or interact with the specific variables and functions of an Object

# Abstraction - isolate the impact of changes made to the code so the change will
# only affect the variables shown and not the outside code

# Polymorphism - allows different classes to have methods with the same name

##### FORMS OF INHERITANCE #####
#SINGLE
#MULTIPLE
#MULTILEVEL
#HIERARCHICAL
#HYBRID - consists of multiple types of inheritance