def print_func(imp_dict, junk_dict, special_item):
    print(f"{special_item} obtained!")
    for key, value in imp_dict.items():
        print(f"{key}: {value}")
    for key, value in junk_dict.items():
        print(f"{key}: {value}")


def Legendary_farming():
    imp_dict = {'shards': 0, 'fragments': 0, 'motes': 0}
    junk_dict = {}
    while_condition = False
    while True:
        items = input().lower()
        items = items.split()

        for value, materials in zip(items[0::2], items[1::2]):
            materials = materials.lower()
            value = int(value)

            if materials in ['shards', 'fragments', 'motes']:
                if materials not in imp_dict:
                    imp_dict[materials] = value
                else:
                    imp_dict[materials] += value

                if imp_dict[materials] >= 250:
                    imp_dict[materials] -= 250
                    special_item = ''
                    if materials == 'shards':
                        special_item = 'Shadowmourne'
                    elif materials == "fragments":
                        special_item = 'Valanyr'
                    elif materials == "motes":
                        special_item = 'Dragonwrath'
                    print_func(imp_dict, junk_dict, special_item)
                    while_condition = True
            else:
                if materials not in junk_dict:
                    junk_dict[materials] = value
                else:
                    junk_dict[materials] += value
            if while_condition:
                break
        if while_condition:
            break


Legendary_farming()