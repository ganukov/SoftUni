from Object_oriented_programming.Inheritance.Inheritance_exercise.players_monsters.hero import Hero
from Object_oriented_programming.Inheritance.Inheritance_exercise.players_monsters.elf import Elf

hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
elf = Elf("E", 4)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)