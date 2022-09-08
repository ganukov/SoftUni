from Object_oriented_programming.Encapsulation.Encapsulation_exercise.wild_cat_zoo.animal import Animal


class Lion(Animal):
    MONEY_FOR_CARE = 50

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, self.MONEY_FOR_CARE)
