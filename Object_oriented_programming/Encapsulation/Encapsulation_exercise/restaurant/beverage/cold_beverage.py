from Object_oriented_programming.Encapsulation.Encapsulation_exercise.restaurant.beverage.beverage import Beverage


class ColdBeverage(Beverage):
    def __init__(self, name, price,milliliters):
        super().__init__(name, price,milliliters)
