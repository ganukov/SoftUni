from Object_oriented_programming.Inheritance.Inheritance_exercise.Zoo.lizard import Lizard
from Object_oriented_programming.Inheritance.Inheritance_exercise.Zoo.mammal import Mammal
from Object_oriented_programming.Inheritance.Inheritance_exercise.Zoo.snake import Snake

mammal = Mammal("Stella")
print(mammal.__class__.__bases__[0].__name__)
print(mammal.name)
lizard = Lizard("John")
print(lizard.__class__.__bases__[0].__name__)
print(lizard.name)
