from Object_oriented_programming.Inheritance.Inheritance_exercise.Shop.product import Product


class Drink(Product):
    quantity = 10

    def __init__(self, name):
        super().__init__(name,self.quantity)
