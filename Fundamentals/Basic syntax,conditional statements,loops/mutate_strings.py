word_1 = input()
word_2 = input()

for i in range(len(word_1)):
    if word_1[i] != word_2[i]:
        word_1 = word_1[:i] + word_1[i:i + 1].replace(word_1[i], word_2[i], 1) + word_1[i + 1:]
        print(word_1)