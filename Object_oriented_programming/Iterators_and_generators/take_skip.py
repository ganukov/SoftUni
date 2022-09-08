class take_skip:
    number = 0

    def __init__(self, step, count):
        self.step = step
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):

        while self.count > 0:
            l = self.number
            self.count -= 1
            self.number += self.step
            return l

        else:
            raise StopIteration


numbers = take_skip(10, 5)

for number in numbers:

    print(number)