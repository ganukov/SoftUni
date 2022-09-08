countries = input().split(', ')
capitals = input().split(', ')
new_ = dict(zip(countries, capitals))

for key, value in new_.items():
    print(f"{key} -> {value}")
