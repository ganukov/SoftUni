from Object_oriented_programming.Inheritance.Inheritance_exercise.Shop.product import Product


class Food(Product):
    quantity = 15

    def __init__(self, name):
        super().__init__(name,self.quantity)



