def valid_pass(password):
    digits_count = 0
    lenght_check = 0
    digit_check = 0
    symbol_check = 0
    symbols = "''""!@#$%^&*()_-+={}[]"

    if 6 <= len(password) <= 10:
        lenght_check += 1
    for i in password:
        if i.isdigit():
            digits_count += 1
            if digits_count >= 2:
                digit_check += 1
        if i in symbols:
            symbol_check += 1
    if lenght_check != 1:
        print("Password must be between 6 and 10 characters")
    if symbol_check != 0:
        print("Password must consist only of letters and digits")
    if digit_check < 1:
        print("Password must have at least 2 digits")

    if lenght_check == 1 and digit_check >= 1 and symbol_check == 0:
        print("Password is valid")


password = input().upper()
valid_pass(password)
