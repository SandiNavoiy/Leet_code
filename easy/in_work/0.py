class SparseArray:
    def __init__(self, *args):
        self._values = list(args)

    @property
    def values(self):
        return tuple(self._values)

    def __getitem__(self, number):
        if number <= len(self._values):
            return self._values[number]
        else:
            self._values.extend([None] * (number - len(self._values)))
            self._values.append(None)

    def __setitem__(self, number, value=None):
        if number > len(self._values):
            self._values.extend([None] * (number - len(self._values)))
            self._values.insert(number, value)
        else:
            self._values[number] = value

    def __delitem__(self, item):
        if 0 <= int(item) < len(self._values):
            self._values[int(item)] = None

    def __len__(self):
        return len(self._values)


array = SparseArray()
print(array.values)
array[5] = 4

array[0] = 13
array[10] = 23
array[5] = 81
array[7] = 100
print(array.values)
print(len(array))
print(array[20])
print(array.values)
