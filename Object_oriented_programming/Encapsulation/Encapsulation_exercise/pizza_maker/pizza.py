from Object_oriented_programming.Encapsulation.Encapsulation_exercise.pizza_maker.topping import Topping


class Pizza:
    def __init__(self, name, dough, toppings_capacity):
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError('The name cannot be an empty string')
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value == "":
            raise ValueError('You should add dough to the pizza')
        self.__dough = value

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        if value <= 0:
            raise ValueError("The topping's capacity cannot be less or equal to zero")
        self.__toppings_capacity = value

    def add_topping(self, topping: Topping):

        if topping.topping_type not in self.toppings:
            if self.toppings_capacity == 0:
                raise ValueError('Not enough space for another topping')
            self.toppings[topping.topping_type] = topping.weight
            self.__toppings_capacity -= 1

        else:
            if self.toppings_capacity == 0:
                raise ValueError('Not enough space for another topping')
            self.toppings[topping.topping_type] += topping.weight
            self.__toppings_capacity -= 1

    def calculate_total_weight(self):

        return self.dough.weight + sum(self.toppings.values())
