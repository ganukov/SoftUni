# What is a Polymorphism?
# Overloading Built-in Methods
# Duck Typing
# What is an Abstraction?
    # abc module
    # @abstractmethod

#What is a Polymorphism?
# poly(many) morphism(forms)
# its the ability to present the same interface for different underlying forms
# though the interface of their base class
#e.g., Square and Triangle inherit Shape,so their instances can be used
# from an instance of type Shape
# a subclass can override a method of its superclass
#e.g., both are shapes and have area
# Overridваме метод в родителския клас!!!
# Without Polymorphism
    # A type check may be required before performing an action on an object
    # to determinate the correct method to call
    # e.g., we will have to use a lot of IF/ELSE checks


# Overloading Built-in Methods
# change the behavior of functions like abs,len,sum
# to do this , you only need to define the special method in your class
#e.g.,__...__

#__lt__ --> '<'
#__le__ --> '<='
#__eq__ --> '=='
#__ne__ --> '!='
#__gt__ --> '>'
#__ge__ --> '>='

#Operator Overloading
#An operator behaves differently based on the type of the operands


#Duck Typing
#its type system used in dynamic languages
#we don`t care about objects`s types , but whether
# they have the methods we need !
# you call same method of totally different objects
# which happens to have the same NAME METHOD/ ITS NOT POLYMORPHISM

###ABSTRACTION###
#if we use abstraction its for us to make sure we push POLYMORPHISM
#for a class to be abstract it should have atleast
# 1 @abstractmethod and to inherit ABC from abc