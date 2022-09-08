word = input()
second_word = input()
result = ""

while word in second_word:
    second_word = second_word.replace(word, "")
print(second_word)