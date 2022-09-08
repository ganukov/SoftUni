import abc


class Animal(abc.ABC):
    def __init__(self, species):
        self.species = species

    def get_species(self):
        return self.species

    @abc.abstractmethod
    def get_sound(self):
        pass


class Dog(Animal):
    def __init__(self, species):
        super().__init__(species)

    def get_sound(self):
        return 'woof'


class Cat(Animal):
    def __init__(self, species):
        super().__init__(species)

    def get_sound(self):
        return 'meow'


class Chicken(Animal):
    def __init__(self, species):
        super().__init__(species)

    def get_sound(self):
        return 'quack'


def animal_sound(animals: list):
    for animal in animals:
        if isinstance(animal, Animal):
            print(animal.get_sound())


# animals = [Animal('cat'), Animal('dog')]


## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
animal_sound(animals)
