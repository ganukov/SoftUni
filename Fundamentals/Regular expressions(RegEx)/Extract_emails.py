import re
text = input()
user = r'( |^)[a-zA-Z0-9]+((\.|\-|\_)[a-zA-Z0-9]+)*'
host = r'[a-zA-Z]+(-[a-zA-Z]+)*(\.[a-zA-Z]+(-[a-zA-Z]+)*)+'
pattern = rf'{user}@{host}'

emails = re.finditer(pattern,text)

for email in emails:
    print(email[0])