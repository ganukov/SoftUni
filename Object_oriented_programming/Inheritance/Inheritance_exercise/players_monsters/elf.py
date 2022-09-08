from Object_oriented_programming.Inheritance.Inheritance_exercise.players_monsters.hero import Hero


class Elf(Hero):
    def __init__(self, username, level):
        super().__init__(username, level)

    def __str__(self):
        return f'{self.username} of type {self.__class__.__name__} has level {self.level}'
