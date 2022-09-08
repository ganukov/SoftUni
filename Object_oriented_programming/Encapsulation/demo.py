            ###ENCAPSULATION###

    #Definition
    #Name Mangling a Variable
    #Name Mangling a Method
    #Built-in Functions for Accessing  Attributes

###Definition = Packing of data and functions into a single component,
###allows us to put restrictions and can prevent accidental modification
###the Variable can ONLY BE CHANGED BY AND OBJECT`S METHOD !!!
####methods and variables in PYTHON are public by default!
####encapsulation is performed by convention not enforced by the language
###########ACCESS MODIFIERS##########
#a#Using single underscore - _
#b#Using double underscore - __ (making it 'private')
#c#Using getter and setter methods to access private variables
####Its convention to diff them into three categories - public,protected,private!!!

######AAAA########

#using _ is just a convention - should be treatec as non-public method/variable

#########BBBB#######
#using __ invokes name mangling,mangling is used for attributes that one class
#DOES NOT WANT SUBCLASSES TO USE
#THE ACCSES IS NOT RESTICTED AND ITS STILL POSSIBLE TO ACEES OR MODIFY FROM OUSIDE!

    #########NAME MANGLING A VARIABLE###########
#ITS USED TO SHOW THAT THE VARIABLE IS NOT TO BE ACCESSED OUSIDE ITS CLASS!


    #########GETTER AND SETTER METHODS#########
        #def get_age(self):
        #   print(self.__age)   #########GETTER########

        #def set_age(self,age):
        #   self.__age = age    #########SETTER########
#we define getters and setters in python by using properties,
#by defining properties you can change the internal implementation of a class,
#without affecting the program
        #class Person:
        #   def __init__(self,age=0):
        #   @property
        #   def age(self):
        #       return self.__age
        #   @age.setter
        #   def age(self,age):
        #       if age<18:self.__age = 18
        #       else: self.__age = age
#you use Python properties to APPLY RULES to an attribute
        #class Person:
        #   def __init__(self,name,age):
        #       self.name = name
        #       self.age = age
        #   @property
        #   def age(self):
        #       return self.__age
        #   @age.setter
        #   def age(self,value):
        #       if value <= 0:
        #           raise Exception('Age must be greater than zero')
        #       self.__age = value

    ########Mangling a Method ###########
#its a class method that should only be called from INSIDE THE CLASS where it is defined!!!!
    ##class Person:
    ##  def __init__(self):
    ##      self.first_name = 'Peter'
    ##      self.last_name = 'Parker'

    ##  def __full_name(self):
    ##      return f'{self.first_name} {self.last_name}'

    ## def info(self):
    ##      return self.__full_name()

    ## person = Person()
    ## print(person.info()) ## Peter Parker
    ## print(person.__full_name()) ## ATTRIBUTEERROR
    ## print(person._Person__full_name()) # Peter Parker

###BUILT IN FUNCTIONS ###

# getattr() - used to access the attribute of an object
#returns the value of the named attribute

## hasattr() - checks if an attribute exist or not
#returns True if the object has the given named attribute and False if it does not

## setattr() - used to set the value of the attribute
# returns None

## delattr() - deletes an attribute from the object
#after deleting the attribute if u call it is raises AttributeError