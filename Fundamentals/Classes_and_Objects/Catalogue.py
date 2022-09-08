class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.product = []

    def add_product(self, product_name):
        self.product.append(product_name)

    def get_by_letter(self, first_letter: str):
        new = []
        if len(self.product) > 0:
            for each in self.product:
                if each[0] == first_letter:
                    new.append(each)
        return new

    def __repr__(self):
        new_line = "\n"
        return f"Items in the {self.name} catalogue:{new_line}{new_line.join(sorted(self.product))}"


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)