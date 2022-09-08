from Object_oriented_programming.Inheritance.Inheritance_exercise.Shop.product import Product
from Object_oriented_programming.Inheritance.Inheritance_exercise.Shop.food import Food
from Object_oriented_programming.Inheritance.Inheritance_exercise.Shop.drink import Drink
from Object_oriented_programming.Inheritance.Inheritance_exercise.Shop.product_repository import ProductRepository


food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.products)
print(repo.find("water"))
repo.find("apple").decrease(5)
print(repo)