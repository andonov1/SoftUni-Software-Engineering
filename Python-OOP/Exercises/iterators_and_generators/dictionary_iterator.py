class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = list(dictionary.items())
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= len(self.dictionary):
            raise StopIteration
        result = self.dictionary[self.i]
        self.i += 1
        return result


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)