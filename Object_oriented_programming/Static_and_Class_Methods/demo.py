# Methods and Decorators
# Static Methods
# Class Methods #
# #1.can change CLASS related things
# #2.can make instances of the CLASS


        ###Static Methods###
#           @staticmethod ---> Decorator           #
#   it cannot modify and know nothing about the CLASS
#   it doesnt take self/and cant be in or outside the Class
        #### Example for Static Method#### ---> person.py
#   Calling it through the instance`s name ---> Person.is_adult(5) ---> correct way
# Avoids accidentals modifications of the code from someone reading it
# Its easier to test cuz its independent fromthe rest of the CLASS



        ###Class Methods###
#           @classmethod ---> Decorator
# Its bound to the class and not the OBJECT of the class
# It can modify a class stake that will apply for all the instances of the class
        ####Example for Classic Method#### ----> student.py
# we use it for creating new controlled instances of the CLASS

#Example#
# class Pizza:
#   def __init__(self,ingredients):
#       self.ingredients = ingredients
#   @classmethod
#   def pepperoni(cls):
#       return cls(['tomato sauce','parmesan','pepperoni'])
#
#
#pizza = Pizza.pepperoni() ==== 'tomato sauce','parmesan','pepperoni'

#####Overriding using CLASS METHODS#####
