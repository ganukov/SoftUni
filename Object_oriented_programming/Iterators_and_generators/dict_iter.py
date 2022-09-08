class dictionary_iter:
    def __init__(self, info: dict):
        self.info = info

    def __iter__(self):
        for pair in self.info.items():
            yield pair


result = dictionary_iter({1: "1", 2: "2"})

for x in result:
    print(x)

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
