from Object_oriented_programming.Encapsulation.Encapsulation_exercise.restaurant.food.main_dish import MainDish


class Salmon(MainDish):
    GRAMS = 22

    def __init__(self, name, price):
        super().__init__(name, price, self.GRAMS)

