product_name = input()
town = input()
weight = float(input())

if town == "Sofia":
    if product_name == "coffee":
        print(weight * 0.50)
    elif product_name == "water":
        print(weight * 0.80)
    elif product_name == "sweets":
        print(weight * 1.45)
    elif product_name == "beer":
        print(weight * 1.20)
    elif product_name == "peanuts":
        print(weight * 1.60)
elif town == "Plovdiv":
    if product_name == "coffee":
        print(weight * 0.40)
    elif product_name == "water":
        print(weight * 0.70)
    elif product_name == "beer":
        print(weight * 1.15)
    elif product_name == "sweets":
        print(weight * 1.30)
    elif product_name == "peanuts":
        print(weight * 1.50)
elif town == "Varna":
    if product_name == "coffee":
        print(weight * 0.45)
    elif product_name == "water":
        print(weight * 0.70)
    elif product_name == "beer":
        print(weight * 1.10)
    elif product_name == "sweets":
        print(weight * 1.35)
    elif product_name == "peanuts":
        print(weight * 1.55)

