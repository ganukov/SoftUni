text = input().split()

new_text = [x for x in text if len(x) % 2 == 0]
print("\n ".join(new_text))