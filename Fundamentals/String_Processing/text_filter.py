banned_words = input().split(", ")
text = input()

for each in banned_words:
    while each in text:
        text = text.replace(each,"*" * len(each))
print(text)