class PizzaDelivery:
    def __init__(self, name: str, price: float, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
        if not self.ordered:
            if ingredient in self.ingredients:
                self.ingredients[ingredient] += quantity
                self.price += quantity * price_per_quantity
            else:
                self.ingredients[ingredient] = quantity
                self.price += quantity * price_per_quantity
        else:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):
        if not self.ordered:
            if ingredient not in self.ingredients:
                return f'Wrong ingredient selected! We do not use {ingredient} in {self.name}!'
            elif ingredient in self.ingredients and quantity > self.ingredients[ingredient]:
                return f'Please check again the desired quantity of {ingredient}!'
            else:
                self.ingredients[ingredient] -= quantity
                self.price -= quantity * price_per_quantity
        else:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def make_order(self):
        self.ordered = True
        return f"You've ordered pizza {self.name} prepared with {', '.join([str(k) + ': ' + str(v) for k, v in self.ingredients.items()])} and the price will be {self.price}lv."


margarita = PizzaDelivery('Margarita', 12, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('cheese', 1, 2)
margarita.add_extra('mozzarella', 1, 2.5)
margarita.remove_ingredient('bacon', 1, 5)
print(margarita.remove_ingredient('tomatoes', 2, 2))
print(margarita.remove_ingredient('tomatoes', 1, 2))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('mozzarella', 1, 2))
