n = int(input())
garage = {}

for i in range(n):
    cars_info = input().split('|')
    car = cars_info[0]
    mileage = int(cars_info[1])
    fuel = int(cars_info[2])
    garage[car] = {'miles': mileage, 'litres': fuel}

while True:
    command = input().split(' : ')

    if command[0] == 'Stop':
        for item in garage:
            print(f'{item} -> Mileage: {garage[item]["miles"]} kms, Fuel in the tank: {garage[item]["litres"]} lt.')
        break

    if command[0] == 'Drive':
        car = command[1]
        distance = int(command[2])
        new_fuel = int(command[3])
        if garage[car]['litres'] < new_fuel:
            print(f'Not enough fuel to make that ride')
        else:
            garage[car]['miles'] += distance
            garage[car]['litres'] -= new_fuel
            print(f'{car} driven for {distance} kilometers. {new_fuel} liters of fuel consumed.')
        if garage[car]["miles"] >= 100000:
            garage.pop(car)
            print(f'Time to sell the {car}!')
    elif command[0] == 'Refuel':
        car = command[1]
        refill = int(command[2])
        new = 0
        while garage[car]['litres'] < 75:
            garage[car]['litres'] += 1
            new += 1
            refill -= 1
            if garage[car]['litres'] == 75 or refill == 0:
                print(f'{car} refueled with {new} liters')
                break
    elif command[0] == 'Revert':
        car = command[1]
        kilometers = int(command[2])
        garage[car]['miles'] -= kilometers
        if garage[car]['miles'] < 10000:
            garage[car]['miles'] = 10000
        else:
            print(f'{car} mileage decreased by {kilometers} kilometers')
