from Object_oriented_programming.Encapsulation.Encapsulation_exercise.restaurant.beverage.hot_beverage import HotBeverage


class Tea(HotBeverage):

    def __init__(self, name, price, milliliters):
        super().__init__(name, price, milliliters)
