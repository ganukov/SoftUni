word = input()
digits = ""
letters = ""
symbols = ""
for each in word:
    if each.isdigit():
        digits += each
    elif each.isalpha():
        letters += each
    else:
        symbols += each
print(digits)
print(letters)
print(symbols)