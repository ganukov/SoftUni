n = int(input())
heroes = {}

for each in range(n):
    heroes_info = input().split()
    names = heroes_info[0]
    hp = int(heroes_info[1])
    mp = int(heroes_info[2])
    heroes[names] = {'hp':hp,'mp':mp}

while True:
    command = input().split(' - ')

    if command[0] == 'End':
        for h in heroes:
            print(f"{h}\n  HP: {heroes[h]['hp']}\n  MP: {heroes[h]['mp']}")
        break
    hero_name = command[1]
    if command[0] == 'CastSpell':
        mp_needed = int(command[2])
        spell_name = command[3]
        if heroes[hero_name]['mp'] >= mp_needed:
            heroes[hero_name]['mp'] -= mp_needed
            print(f'{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]["mp"]} MP!')
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif command[0] == 'TakeDamage':
        damage = int(command[2])
        attacker = command[3]
        heroes[hero_name]['hp'] -= damage
        if heroes[hero_name]['hp'] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['hp']} HP left!")
        else:
            heroes.pop(hero_name)
            print(f"{hero_name} has been killed by {attacker}!")

    elif command[0] == 'Recharge':
        amount = int(command[2])
        new = heroes[hero_name]['mp'] + amount
        if new > 200:
            new = 200
            print(f"{hero_name} recharged for {200 - heroes[hero_name]['mp']} MP!")
            heroes[hero_name]['mp'] = 200
        else:
            print(f"{hero_name} recharged for {new - heroes[hero_name]['mp']} MP!")
            heroes[hero_name]['mp'] = new
    elif command[0] == 'Heal':
        heal = int(command[2])
        mew = heroes[hero_name]['hp'] + heal
        if mew > 100:
            mew = 100
            print(f"{hero_name} healed for {100 - heroes[hero_name]['hp']} HP!")
            heroes[hero_name]['hp'] = 100
        else:
            print(f"{hero_name} healed for {mew - heroes[hero_name]['hp']} HP!")
            heroes[hero_name]['hp'] = mew