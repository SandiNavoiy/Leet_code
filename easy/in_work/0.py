class Vector:
    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return f'Vector({", ".join([str(value) for value in self.values])})'

    def __getitem__(self, item):
        if isinstance(item, str):
            item = len(item)

        if 1 <= item <= len(self.values):
            return self.values[item - 1]
        else:
            raise IndexError(f"Индекс {item} находится за пределами вектора")


v = Vector(3, 655, 323, 672, 11, 6)
print(v[1])  # 3
print(v[2])  # 655
print(v["cat"])  # 323
print(v["park"])  # 672
# try:
#     print(v[""])
# except IndexError as e:
#     print(e)
