class SequenceIterator:
    def __init__(self, value):
        self.value = value[::2] + value[1::2]
        self.index = 0

    def __iter__(self):
        return self
    def __next__(self):
        if self.index == len(self.value):
            raise StopIteration
        t = self.value[self.index]
        self.index += 1
        return t

#
container = SequenceIterator([1, 5, 4, 6, 43, True, 'hello'])

for i in container:
    print(i)
