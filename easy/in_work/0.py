class Point:
    def __init__(self):
        self.x = None
        self.y = None

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, object):
        if isinstance(object, Point):
            distance = ((self.x - object.x) ** 2 + (self.y - object.y) ** 2) ** 0.5
            return distance
        else:
            print("Передана не точка")
            return None


# Код ниже не удаляйте, он нужен для проверок
p1 = Point()
p2 = Point()
assert isinstance(p1, Point)
assert isinstance(p2, Point)

p1.set_coordinates(1, 2)
assert p1.x == 1
assert p1.y == 2
p2.set_coordinates(4, 6)
assert p2.x == 4
assert p2.y == 6
assert p1.get_distance(p2) == 5.0
p3 = Point()
p3.set_coordinates(10, 10)
p1.set_coordinates(4, 2)
assert p1.get_distance(p3) == 10.0
res = p1.get_distance(10)  # Распечатает "Передана не точка", вернет None
assert (
    res is None
), "Метод get_distance должен возвращать None, если в него была передана не точка"

assert (
    p2.get_distance([1, 2, 3]) is None
)  # Распечатает "Передана не точка", вернет None
