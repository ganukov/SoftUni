class vowels:
    vowel_chars = 'eyuioa'

    def __init__(self, value: str):
        self.value = value
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):

        while self.index < len(self.value):
            if self.value[self.index].lower() not in self.vowel_chars:
                self.index += 1
                continue

            value_to_return = self.value[self.index]
            self.index += 1
            return value_to_return
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
