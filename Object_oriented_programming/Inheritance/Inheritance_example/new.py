from Object_oriented_programming.Inheritance.Inheritance_exercise.Person.person import Person
from Object_oriented_programming.Inheritance.Inheritance_exercise.Person.child import Child

person = Person("Peter", 25)
child = Child("Peter Junior", 5)
print(person.name)
print(person.age)
print(child.__class__.__bases__[0].__name__)
