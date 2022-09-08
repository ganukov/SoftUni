import re

n = int(input())

for each in range(n):
    text = input()

    pattern = r"(\@\#+)([A-Za-z0-9]{6,})(\@\#+)"
    matches = re.match(pattern,text)
    if not matches:
        print(f"Invalid barcode")
    else:
        product_group = []
        for i in matches.group(2):
            if i.isdigit():
                product_group.append(i)
        if not product_group:
            print('Product group: 00')
        else:
            print(f"Product group: {''.join(product_group)}")